import sys
read = sys.stdin.readline

for _ in range(int(read())):
    n, m = map(int, read().split())
    answer = (n * m) // 3
    if (n * m) % 3 > 0:
        answer += 1
    print(answer)
