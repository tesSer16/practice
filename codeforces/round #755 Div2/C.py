import sys
read = sys.stdin.readline

for _ in range(int(read())):
    n = int(read())
    a, b = sorted(list(map(int, read().split()))), sorted(list(map(int, read().split())))
    for i in range(n):
        if a[i] + 1 < b[i]:
            print("NO")
            break
    else:
        print("YES")
