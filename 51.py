number = 6
divisors = []

for i in range(1, number):
    if number % i == 0:
        divisors.append(i)

n = 0

for i in divisors:
    n += i

if n == number:
    print("The number is perfect")
