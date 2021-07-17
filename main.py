from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import create_engine

engine = create_engine("sqlite:///test.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))

    def __repr__(self):
        return "<User %s>" % self.name


def create_test_data(num=2000):
    for i in range(num):
        user = User(name="user_%s" % i)
        session.add(user)
    session.commit()


if __name__ == "__main__":
    # Base.metadata.create_all(engine, checkfirst=True)

    # first create some test data
    # create_test_data()

    uids = ",".join([str(x) for x in range(400000)])
    from sqlalchemy.sql import text

    uids_in = text(f"user.id in ({uids})")
    print(session.query(User).filter(uids_in).all())

    from sqlalchemy import bindparam

    # print(
    #     session.query(User)
    #     .filter(User.id.in_(bindparam("x", range(400000), expanding=True, literal_execute=True)))
    #     .all()
    # )
