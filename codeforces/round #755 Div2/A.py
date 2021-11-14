import sys
read = sys.stdin.readline

for _ in range(int(read())):
    u, v = map(int, read().split())
    print(u * u, -v * v)
