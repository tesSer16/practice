import sys


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


for _ in range(int(input())):
    M, N, x, y = map(int, sys.stdin.readline().split())

