# sqlite-999
resolve SQLITE_MAX_VARIABLE_NUMBER problem

## python
```bash
python3 -m venv ./venv
source ./venv/bin/activate
pip install sqlalchemy
```

## prepare sqlite

3.32.0 SQLITE_MAX_VARIABLE_NUMBER defaults to 32766, the version less than this is 999.

check version
```
sqlite3 -version

> 3.28.0 2019-04-15 14:49:49 378230ae7f4b721c8b8d83c8ceb891449685cd23b1702a57841f1be40b5daapl
```

```sql
sqlite3 test.db

> create table user (id integer primary key autoincrement, name text);
```

## solution

1. Solution1:

```python
Query.filter(text("table.col in (1,2,3,4 ....)"))
```

2. Solution2: sqlalchemy >= 1.4 bindparam() with literal_execute=True

```python
Query.filter(Table.Column.in_(bindparam("xxx", range(300000), literal_execute=True)))
```
