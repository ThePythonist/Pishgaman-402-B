import time


def factorial(x):
    if x == 1:
        # return x
        return 1
    else:
        return x * factorial(x - 1)


def main():
    entry = input("Enter any number : ")

    try:
        entry = int(entry)
        try:
            print(factorial(entry))
        except RecursionError:
            print("Number must be positive")
            print("You have to wait 5 seconds to try again")
            time.sleep(5)
            main()
    except ValueError:
        print("Entry must be an integer number")
        print("You have to wait 5 seconds to try again")
        time.sleep(5)
        main()


main()
