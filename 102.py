import jdatetime

today = str(jdatetime.datetime.now())
today = today.split()
day = today[0]
time = today[1][0:5]

print(f"Emrooz {day} ast va saat {time} ast")
