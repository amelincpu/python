import os
import sys
import sqlite3

test_db = sqlite3.connect(os.path.join(sys.path[0], 'test2.db'))
db_operation = test_db.cursor()
db_operation.execute("SELECT * FROM switches")
print(db_operation.fetchall())

show_db = db_operation.execute("SELECT * FROM switches")
for line in show_db:
    print(line)


new_db = sqlite3.connect(os.path.join(sys.path[0], 'new.db'))
db_operation = new_db.cursor()
db_operation.execute("""CREATE TABLE IF NOT EXISTS switches (
                        id integer PRIMARY KEY,
	                    hostname text NOT NULL,
                        model text,
                        ip text)""")
to_db = [(1, 'sw01', '2960', '1.1.1.1'), 
        (2, 'sw02', '3750', '1.1.1.2'),
        (3, 'sw03', '3850', '1.1.1.3'),
        (4, 'sw04', '2960', '1.1.1.4')]
to_db_operation = "INSERT INTO switches values (?, ?, ?, ?)"
db_operation.executemany(to_db_operation, to_db)
new_db.commit()
db_operation.execute("SELECT * FROM switches")
print(db_operation.fetchall())
new_db.close()
