import sys
read = sys.stdin.readline


def solve():
    cnt = 0
    for i in range(n - 1, 0, -1):
        if i > 0 and arr[i] == 0:
            return -1
        z_cnt = 0
        for j in range(i):
            while arr[j] >= arr[i]:
                arr[j] //= 2
                cnt += 1
            if arr[j] == 0:
                z_cnt += 1
            if z_cnt == 2:
                return -1

    return cnt


for _ in range(int(read())):
    n = int(read())
    arr = list(map(int, read().split()))
    print(solve())
