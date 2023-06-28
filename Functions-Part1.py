def checknumber(x):
    if type(x) in [int, float]:
        print("Okay continue")
        return "Number"
    else:
        print("Not okay")
        return "Not Number"


checknumber(10)


# if checknumber("X") == "Number":
#     print("Yes")
# else:
#     print("No")

# -------------------------------------------

# def checknumber(x):
#     if x % 2 == 0:
#         print("Even")
#         # return "Even"
#     else:
#         print("Odd")
#         # return "Odd"
#
#
# # checknumber(7)
# # print(checknumber(14))
#
# if checknumber(8) == "Even":
#     print("Pasokh zoj ast")
