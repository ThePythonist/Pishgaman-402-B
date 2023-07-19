lines = open("words.txt").read().split("\n")
open("oneline.txt", "w").write("".join(lines))
