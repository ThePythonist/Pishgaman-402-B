def myhash(x):
    if len(str(x)) == 1:
        return x
    else:
        figures = []
        for i in str(x):
            figures.append(int(i))
        x = sum(figures)
        return myhash(x)


print(myhash(345345))
