def prime_status(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    print(divisors)
    print("Prime") if len(divisors) == 2 else print("Not Prime")
    prime_status(number)

number = int(input("Enter any number to check : "))
prime_status(number)

# def prime_status(number):
#     divisors = [i for i in range(1, number + 1) if number % i == 0]
#     print(divisors)
#     return "Prime" if len(divisors) == 2 else "Not Prime"
#
#
# number = int(input("Enter any number to check : "))
# print(prime_status(number))
