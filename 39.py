items = [
    "bmw",
    21,
    True,
    6.7,
    14,
    15,
    False,
    False,
    "Tehran"
]

words = []

for i in items:
    if type(i) == str:
        words.append(i)

print(words)
