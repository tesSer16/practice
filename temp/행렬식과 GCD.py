def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m % n)


N = int(input())
fibo = [0, 1]
div = 10 ** 9 + 7
for i in range(N):
    fibo.append((fibo[-1] + fibo[-2]) % div)

print(sum(fibo[gcd(i, N + 1)] for i in range(2, N + 2)) % div)
