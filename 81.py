name = input("Enter your name : ")
expire = 12

msg = """
Moshtarak gerami {n}
tanha {e} rooz digar az zaman basteye shoma
baghi mande ast.
""".format(n=name.capitalize(), e=expire)

print(msg)
