scores = {
    "fizik1": 14,
    "mabani computer": 20,
    "zaban omomi": 18,
    "andishe eslami": 7,
    "riazi1": 12,
}

for k, v in scores.items():
    if v >= 10:
        print(k, ": Passed : ", v)
    else:
        print(k, ": Failed : ", v)

# SUM = 0
# for i in scores.values():
#     SUM += i
#
# average = SUM / len(scores)
average = sum(scores.values()) / len(scores)
print(average)
