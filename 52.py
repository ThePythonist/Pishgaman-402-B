numbers = []

for i in range(4):
    entry = input("Entry : ")

    try:
        entry = float(entry)
        numbers.append(entry)

    except ValueError :
        print("Not a number")

print(numbers)
