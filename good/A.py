primes = [2]
for n in range(3, 110):
    for p in primes:
        if n % p == 0:
            break
    else:
        primes.append(n)

N = int(input())
for i in range(len(primes) - 1):
    value = primes[i] * primes[i + 1]
    if value > N:
        print(value)
        break
