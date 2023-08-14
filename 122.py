import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()


def create_table(table_name, fields):
    columns = []

    for i in range(int(fields)):
        columns.append(input("Column : "))

    command = "CREATE TABLE {} {};".format(table_name, tuple(columns))

    for i in columns:
        open(f"{table_name}.txt", "a+").write(i + "\n")

    cur.execute(command)

    con.commit()
    con.close()
    print("Done")


def select_from(table_name):
    cur.execute(f"PRAGMA table_info({table_name});")
    fields = cur.fetchall()
    # fields = open(f"{table_name}.txt").readlines()
    try:
        entry = input("Do you need any filter (yes/no) ? : ")
        if entry == "yes":
            column = input("Column : ")
            condition = input("Condition : ")

            command = f"SELECT * FROM {table_name} WHERE {column} {condition} ;"
            cur.execute(command)
            values = cur.fetchall()
            print(values)

        elif entry == "no":
            command = f"SELECT * FROM {table_name};"
            cur.execute(command)
            values = cur.fetchall()

            fields2 = []
            for i in range(len(fields)):
                fields2.append(fields[i][1])

            records = []

            for i in values:
                records.append(dict(zip(tuple(fields2), i, )))

            for i in records:
                print(i)

        else:
            print("Invalid input. Try again")
            select_from(input("Enter table name : "))
    except sqlite3.OperationalError as error:
        print(error)


def insert_into(table_name):
    cur.execute(f"PRAGMA table_info({table_name});")
    records = cur.fetchall()
    # records = open(f"{table_name}.txt").readlines()
    values = []

    for i in range(len(records)):
        entry = input(f"{records[i][1]} : ")
        values.append(entry)

    command = "INSERT INTO {} VALUES {};".format(table_name, tuple(values))
    cur.execute(command)
    con.commit()
    print("Done")


def main():
    query = input("""
1 : Create table
2 : Insert into table
3 : Select from table
""")

    if query == "1":
        create_table(input("Table name : "), input("Number of table fields : "))
    elif query == "2":
        insert_into(input("Table name : "))
    elif query == "3":
        select_from(input("Table name : "))
    else:
        print("Invalid Entry Try Again")
        main()


main()
