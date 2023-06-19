number = input("Enter any number : ")
try:
    number = int(number)
    print("It is a number")
except ValueError:
    print("It is not a number")

# ------------------------------------------------

# try:
#     # x = int("ali")
#     print(x)
# except (NameError, ValueError):
#     print("Something went wrong")

# ------------------------------------------------

# try:
#     print(x)
# except NameError:
#     print("X not found")
#
# print("Edame")

# ------------------------------------------------

# try:
#     x = int("ali")
#     # print(x)
# except (NameError, ValueError) as argument:
#     print(argument)
#
# print("edameye barname")
