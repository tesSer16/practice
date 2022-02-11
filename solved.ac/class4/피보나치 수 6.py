def f(n):
    if n in m:
        return m[n]

    if n % 2 == 0:
        m[n] = (f(n // 2) ** 2 +
                2 * f(n // 2) * f(n // 2 - 1)) % div
    else:
        m[n] = (f(n // 2 + 1) ** 2 + f(n // 2) ** 2) % div

    return m[n]


div = 1_000_000_007
m = {0: 0, 1: 1, 2: 1}

print(f(int(input())))
