import sys
read = sys.stdin.readline


for _ in range(int(read())):
    l, r, k = map(int, read().split())
    cnt = 0
    if l == r > 1:
        print("YES")
    elif (r - l + 1) // 2 + (l % 2) * (r % 2) <= k:
        print("YES")
    else:
        print("NO")
