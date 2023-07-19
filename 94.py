# lines = open("words.txt").readlines()[::-1]
# output = "".join(lines)
# open("reversed_words.txt", "w").write(output)
# print('Done')

lines = open("words.txt").readlines()
rev = []

for line in lines:
    rev.append(line[::-1])

output = "".join(rev)
open("reversed_words.txt", "w").write(output)
print('Done')