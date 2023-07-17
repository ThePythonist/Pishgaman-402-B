def f1():
    lines = open("words.txt").readlines()
    lines.sort(key=len)
    maximum = lines[-1]
    print(len(maximum))
    print(maximum)


# f1()

def f2():
    lines = open("words.txt").readlines()
    maximum = max(lines, key=len)
    print(len(maximum))
    print(maximum)


# f2()

def f3():
    lines = open("words.txt").readlines()
    maximum = max(lines, key=len)
    # minimum = min(lines, key=len)
    for i in lines:
        if len(i) == len(maximum):
        # if len(i) == len(minimum):
            print(i)


f3()
