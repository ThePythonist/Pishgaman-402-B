items = ["sabanet", "irancell", "iran khodro", "irancell", "sabanet"]
# unique_items = []
#
# for i in items:
#     if i not in unique_items:
#         unique_items.append(i)
#
# ----------------------------------------------------------------
# unique_items = []
# unique_items = [i for i in items if i not in unique_items]
# print(unique_items)
# ----------------------------------------------------------------
print(list(set(items)))
