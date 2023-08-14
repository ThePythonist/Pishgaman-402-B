import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS students (name, major, grade);")

# cur.execute("INSERT INTO students VALUES ('Mohsen','Mohandesi Computer','17.05');")
# cur.execute("INSERT INTO students VALUES ('Ayda','Mohandesi Sanaye','18.31');")
# cur.execute("INSERT INTO students VALUES ('Shima','Theater','16.00');")
# cur.execute("INSERT INTO students VALUES ('Saba','Shimi','19.00');")
# cur.execute("INSERT INTO students VALUES ('Kian','Mohandesi Bargh','14.50');")

cur.execute("SELECT * FROM students;")
records = cur.fetchall()
for i in records:
    if float(i[-1]) >= 17 :
        print(i)
# print(records)

con.commit()
con.close()
print('Done')
