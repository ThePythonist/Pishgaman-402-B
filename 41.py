items = []

for i in range(4):
    x = int(input("Enter any number : "))
    items.append(x)

items.sort()
items = items[::-1]
print(items)
