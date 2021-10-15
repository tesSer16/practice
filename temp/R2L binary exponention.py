def R2L(g, k, N):
    if g == 0:
        return 0

    A, B = 1, g
    k = format(k, 'b')
    t = len(k) - 1

    for i in range(t + 1):
        if k[i] == '1':
            A = (A * B) % N
        B = (B * B) % N

    return A


g = int(input())
k = int(input())
N = int(input())
print(R2L(g, k, N))
