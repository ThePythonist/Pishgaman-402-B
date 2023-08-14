import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS employees (name, code, job);")

# students = [
#     {"name": "Sajad", "code": "40211", "job": "Backend Developer"},
#     {"name": "Amir", "code": "40212", "job": "Frontend Developer"},
#     {"name": "Sarina", "code": "40213", "job": "Security Engineer"},
#     {"name": "Zahra", "code": "40214", "job": "DevOps Engineer"},
#     {"name": "Elisa", "code": "40215", "job": "Civil Engineer"},
# ]
#
# for person in students:
#     cur.execute(f"INSERT INTO employees VALUES (?,?,?)", (person['name'], person['code'], person['job']))
#     con.commit()


# cur.execute("DELETE FROM employees;")

cur.execute("SELECT * FROM employees;")
records = cur.fetchall()
# for i in records:
#     print(i)
print(records)

con.commit()
con.close()
print('Done')
