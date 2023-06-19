number = 11
divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print(divisors)
# if divisors == [1, number]:
if len(divisors) == 2:
    print("The number is prime")
else:
    print("The number isnt prime")
