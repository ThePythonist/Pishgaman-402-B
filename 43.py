office1_shopping_list = ["Khodkar", "Dastmal Kaghazi", "Mouse", "Livan", "A4"]
office2_shopping_list = ["Khodkar", "Mangane", "Mouse", "Keyboard", "A4", "Speaker"]
shopping_list = []

# for i in office1_shopping_list:
#     if i in office2_shopping_list:
#         shopping_list.append(i)

for i in office1_shopping_list:
    for j in office2_shopping_list:
        if i == j:
            shopping_list.append(i)

print(shopping_list)
