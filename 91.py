# lines = open("words.txt").readlines()
# new_words = []
#
# for i in lines :
#     new_words.append(i[:-1])
#
# print(new_words)
# -----------------------------------------------------------
# lines = open("words.txt").read().replace("\n"," ")
# print(lines)
# -----------------------------------------------------------
lines = open("words.txt").read().split("\n")
print(lines)
