def filter_numbers(items):
    # numbers = []
    # for i in items:
    #     if type(i) in [int, float]:
    #         numbers.append(i)
    numbers = [i for i in items if type(i) in [int, float]]
    return numbers


items = [4, True, 12.5, 6.3, "Metallica", 7]
print(filter_numbers(items))

items2 = [19, "PC", "SmartPhone", "TV", 156.3]
print(filter_numbers(items2))
