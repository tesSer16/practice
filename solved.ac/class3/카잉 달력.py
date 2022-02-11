import sys


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


for _ in range(int(input())):
    M, N, x, y = map(int, sys.stdin.readline().split())
    LCM = M * N // gcd(max(M, N), min(M, N))
    for k in range(x, LCM + 1, M):
        if k % N == y % N:
            print(k)
            break
    else:
        print(-1)
