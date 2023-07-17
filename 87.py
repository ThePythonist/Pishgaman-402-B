# lines = open("words.txt").readlines()
# five_letters = ""
#
# for line in lines:
#     if len(line) == 6:
#         five_letters += line
#
# open("fiveletters.txt", "w").write(five_letters)
# print("Done")

lines = open("words.txt").readlines()
five_letters = []

for line in lines:
    if len(line) == 6:
        five_letters.append(line)

output = "".join(five_letters)

open("fiveletters.txt", "w").write(output)
print("Done")
