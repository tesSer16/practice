def R2L(g, k, n):
    if g == 0:
        return 0

    A, B = 1, g
    k = format(k, 'b')

    for ki in k[::-1]:
        if ki == '1':
            A = (A * B) % n
        B = (B * B) % n

    return A


_sum = 0
NUM = 1_000_000_007
for _ in range(int(input())):
    N, S = map(int, input().split())
    _sum += S * R2L(N, NUM - 2, NUM)

print(_sum % NUM)
