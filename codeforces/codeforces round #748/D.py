import sys
read = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for _ in range(int(read())):
    n = int(read())
    arr = list(map(int, input().split()))
    min_val = min(arr)
    s_arr = sorted(set([a - min_val for a in arr]))
    m = len(s_arr)
    if m == 1:
        print(-1)
    else:
        GCD = s_arr[0]
        for i in range(1, m):
            GCD = gcd(GCD, s_arr[i])
        print(GCD)
