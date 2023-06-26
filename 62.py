# word = "Python"
# d = {}
# index = 0
#
# for i in word:
#     d.setdefault(i, index)
#     index += 1
#
# print(d)
# ----------------------------------------
# word = "Python"
# d = {}
#
# for i in range(len(word)):
#     d.setdefault(i, word[i])
#
# print(d)
# ----------------------------------------
# word = "Python"
# d = dict(zip(range(len(word)), word))
# print(d)
# ----------------------------------------
word = "JAVA"
d = tuple(zip(range(len(word)), word))
print(d)
