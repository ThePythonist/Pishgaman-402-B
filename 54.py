numbers = []

while True:
    entry = input("Type something : ")
    if entry == "exit":
        break
    else:
        try:
            entry = float(entry)

            if str(entry)[-2:] == ".0":
                numbers.append(int(entry))
            else:
                numbers.append(entry)

        except ValueError:
            # print("Not a number")
            pass

print(numbers)
print("Max is", max(numbers))
