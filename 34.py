numbers = [1, 2, 3, 4, 5]

# for i in range(6, 11):
#     x = int(input("Enter any number between 6-10 : "))
#     if 6 <= x <= 10:
#         numbers.append(x)
#     else:
#         print("Number must be between 6-10")
#
# print(numbers)


while not len(numbers) == 10:
    x = int(input("Enter numbers (6-10) : "))
    if 5 < x < 11:
        numbers.append(x)
    else :
        print("Invalid Number (Only 6-10)")

print(numbers)
