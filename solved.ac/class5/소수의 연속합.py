N = int(input())
check = [1] * (N + 1)
primes = []
for num in range(2, N + 1):
    if check[num]:
        primes.append(num)
        for n in range(2 * num, N + 1, num):
            check[n] = 0

if primes:
    i, j = 0, 0
    _sum, cnt = 2, 0
    while i <= j:
        if _sum <= N:
            if _sum == N:
                cnt += 1
            j += 1
            if j >= len(primes):
                break
            _sum += primes[j]
        else:
            _sum -= primes[i]
            i += 1
    print(cnt)

else:
    print(0)
