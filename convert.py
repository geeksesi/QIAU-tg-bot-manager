import sqlite3
import hashlib
# import csv

conn_backup = sqlite3.connect('QIAU_CEIT.sql')
c_b = conn_backup.cursor()

conn = sqlite3.connect('QIAU_CEIT.sql')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS all_students;")
c.execute("DROP TABLE IF EXISTS accepted;")
c.execute("DROP TABLE IF EXISTS user;")
c.execute("DROP TABLE IF EXISTS user_meta;")
c.execute("DROP TABLE IF EXISTS class;")
c.execute("DROP TABLE IF EXISTS class_meta;")

c.execute('''CREATE TABLE user
             (id INT PRIMARY KEY NOT NULL, code TEXT NOT NULL, chat_id TEXT, CONSTRAINT code_unique UNIQUE (code))'''
          )
c.execute('''CREATE TABLE user_meta
             (id INT PRIMARY KEY NOT NULL, user_id TEXT NOT NULL, key TEXT, value TEXT NOT NULL, timestamp BIGINT NOT NULL)'''
          )

c.execute('''CREATE TABLE class
             (id INT PRIMARY KEY NOT NULL, name TEXT NOT NULL, type CHAR(20), chat_id TEXT, term INT NOT NULL)'''
          )

c.execute('''CREATE TABLE class_meta
             (id INT PRIMARY KEY NOT NULL, user_id TEXT NOT NULL, key TEXT, value TEXT NOT NULL, timestamp BIGINT NOT NULL)'''
          )

c.execute('''CREATE TABLE messages
             (id INT PRIMARY KEY NOT NULL, class_id TEXT NOT NULL, condition TEXT, text TEXT NOT NULL, timestamp BIGINT NOT NULL)'''
          )

# with open('main.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             md5 = hashlib.md5(row[0].encode('utf-8')).hexdigest()
#             print(f'{line_count} - {md5} ::: {row[1]}')
#             c.execute("INSERT INTO all_students (id,code,type) VALUES (" +
#                       str(line_count) + ", '" + md5 + "', '" + row[1] + "')")
#             line_count += 1
#     print(f'Processed {line_count} lines.')

# c_b.execute("SELECT * ")
conn.commit()
# cursor = conn.execute("SELECT * from all_students")
# for row in cursor:
#     print(f'{row[0]} - {row[1]} :: {row[2]}')
# print("NAME = " + row[1])
# print("ADDRESS = " + row[2])
