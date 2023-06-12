a = 0
b = 1

# for i in range(100):
#     c = a + b
#     a = b
#     b = c
#     print(c)

for i in range(100):
    print(a)
    a, b = b, a + b
