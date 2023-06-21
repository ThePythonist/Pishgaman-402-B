numbers = []

for i in range(4):
    entry = input("Entry : ")

    try:
        entry = float(entry)
        if str(entry)[-2:] == ".0":
            numbers.append(int(entry))
        else:
            numbers.append(entry)

    except ValueError:
        print("Not a number")

print(numbers)
