n = int(input("Chand adad niaz darid : "))
items = []

for i in range(n):
    print("Adad", i + 1, "ra vared konid : ", end="")
    x = int(input())
    items.append(x)

print("Maximum is", max(items))
