def register():
    username = input("Username : ").lower()
    password = input("Password : ")

    open("users.txt", "a").write(username + "\n")
    open("passwords.txt", "a").write(password + "\n")

    print(f"Signed up user {username}")


def signin():
    users = [i[:-1] for i in open("users.txt").readlines()]
    passwords = [i[:-1] for i in open("passwords.txt").readlines()]
    accounts = dict(zip(users, passwords))

    username = input("Username : ").lower()
    password = input("Password : ")

    if username in accounts:
        if password == accounts[username]:
            print("Successfully logged in")
        else:
            print("Password is incorrect")
    else:
        print("Account not found")


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
