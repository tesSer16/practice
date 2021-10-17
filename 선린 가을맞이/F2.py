import sys


def R2L(g, k, N):
    if g == 0:
        return 0

    A, B = 1, g
    k = format(k, 'b')

    A_flag, B_flag = 0, 0
    cnt = 0
    for ki in k[::-1]:
        if not B_flag and float(B).is_integer():
            B = int(B)
            B_flag = 1
        if ki == '1':
            A = (A * B) % N
        B = (B * B) % N

        cnt += 1

    return A


for _ in range(int(input())):
    N = int(sys.stdin.readline())
    t = 17**0.5
    t2 = R2L(2, N + 1, 1000000007)

    a = (R2L(5 + t, N, 1000000007) / (t2) / t * (t + 9))
    b = (R2L(5 - t, N, 1000000007) / (t2) / t * (t - 9))
    print(int((a + b)) % 1000000007)
