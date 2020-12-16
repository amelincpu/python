import os
import sys
import sqlite3

test_db = sqlite3.connect(os.path.join(sys.path[0], 'test.db'))

db_operation = test_db.cursor()

db_operation.execute("SELECT * FROM test")

print(db_operation.fetchall())

show_db = db_operation.execute("SELECT * FROM test")

for line in show_db:
    print(line)


test_db.commit()
