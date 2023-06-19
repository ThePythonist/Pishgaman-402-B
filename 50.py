primes = []

for i in range(1, 100):
    for j in range(2, i):
        if i % j == 0:
            # Yaani yek shomarande peyda shode
            break
    else:
        # Yaani adad aval boode
        primes.append(i)

print(primes)
