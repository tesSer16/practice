for _ in range(int(input())):
    x, n = map(int, input().split())
    k, m = (n - 1) // 4, (n - 1) % 4
    ini = 1 if x % 2 else -1
    result = ini * (1 + 4 * k)

    dir = ini
    for num in range(m):
        if num % 2 == 0:
            dir *= -1
        result += dir * (n - m + num + 1)

    print(result + x)


