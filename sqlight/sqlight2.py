"""."""


import os
import sys
import sqlite3


def print_db_table():
    """Print the whole."""
    for table_line in db_connector.execute('SELECT * FROM switches'):
        print(table_line)


def print_stars():
    """Print 50 stars in the same line to make better output visibility."""
    print('\n', '*'*50, '\n', end='')


print_stars()

data_for_db = [(1, 'sw01', '2960', '1.1.1.1'),
               (2, 'sw02', '3750', '1.1.1.2'),
               (3, 'sw03', '3850', '1.1.1.3'),
               (4, 'sw04', '2960', '1.1.1.4')]

db_connector = sqlite3.connect(os.path.join(sys.path[0], 'test2.db'))
db_connector.execute('DROP TABLE IF EXISTS switches')
db_connector.commit()

with open(os.path.join(sys.path[0], 'new_db.sql')) as sql_script:
    db_connector.execute(sql_script.read())

to_db = 'INSERT INTO switches VALUES (?, ?, ?, ?)'

db_connector.executemany(to_db, data_for_db)
db_connector.commit()

print_db_table()

print_stars()

new_to_db = "INSERT INTO switches VALUES(5, 'sw05', '2960', '1.1.1.5')"
try:
    db_connector.execute(new_to_db)
except sqlite3.IntegrityError as sql_error:
    print('DB error:', sql_error)
db_connector.commit()

print_db_table()

print_stars()

db_connector.close()
