items = [
    "bmw",
    21,
    True,
    6.7,
    14,
    15,
    "Tehran"
]

numbers = []

for i in items:
    # if type(i) == int or type(i) == float:
    if type(i) in [int, float]:
        numbers.append(i)

print(numbers)
