import sys
read = sys.stdin.readline

for _ in range(int(read())):
    a = list(map(int, read().split()))
    if sum(a) % 3:
        print(1)
    else:
        print(0)
