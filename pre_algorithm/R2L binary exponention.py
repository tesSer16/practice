def R2L(g, k, N):
    if g == 0:
        return 0

    A, B = 1, g
    k = format(k, 'b')

    for ki in k[::-1]:
        if ki == '1':
            A = (A * B) % N
        B = (B * B) % N

    return A


print(R2L(*map(int, input().split())))
