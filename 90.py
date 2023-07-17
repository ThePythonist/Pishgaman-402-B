lines = open("words.txt").readlines()
inglist = []

for line in lines :
    # if line[-4:-1] == "ing":
    if "ing" in line[-4:]:
        inglist.append(line)


print(inglist[:100])
