def register():
    username = input("Username : ").casefold()
    password = input("Password : ")

    open("users.txt", "a").write(username+"\n")
    open("passwords.txt", "a").write(password+"\n")

    print(f"Signed up user {username}")


def signin():
    pass
    acconts = {"javad":"123"}


def main():
    operation = input("""
    Choose an operation :
    1 : Register an account
    2 : Sign-in to your account
    """)

    if operation == "1":
        register()
    elif operation == "2":
        signin()
    else:
        print("Invalid entry. Choose 1 or 2")
        main()


main()
