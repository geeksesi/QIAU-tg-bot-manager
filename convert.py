import sqlite3
import hashlib
import csv

conn = sqlite3.connect('QIAU_CEIT.sql')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS all_students;")
c.execute('''CREATE TABLE all_students
             (id INT PRIMARY KEY NOT NULL, code TEXT NOT NULL, type CHAR(20))'''
          )
c.execute("DROP TABLE IF EXISTS accepted;")
c.execute('''CREATE TABLE accepted
             (id INT PRIMARY KEY NOT NULL, code TEXT NOT NULL, type CHAR(20), chat_id TEXT NOT NULL, CONSTRAINT code_unique UNIQUE (code))'''
          )

with open('main.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            md5 = hashlib.md5(row[0].encode('utf-8')).hexdigest()
            print(f'{line_count} - {md5} ::: {row[1]}')
            c.execute("INSERT INTO all_students (id,code,type) VALUES (" +
                      str(line_count) + ", '" + md5 + "', '" + row[1] + "')")
            line_count += 1
    print(f'Processed {line_count} lines.')
conn.commit()
# cursor = conn.execute("SELECT * from all_students")
# for row in cursor:
#     print(f'{row[0]} - {row[1]} :: {row[2]}')
# print("NAME = " + row[1])
# print("ADDRESS = " + row[2])
