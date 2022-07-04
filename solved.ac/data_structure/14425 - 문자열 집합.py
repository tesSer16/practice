import sys
read = sys.stdin.readline


N, M = map(int, read().split())
words = {read() for _ in range(N)}
cnt = 0
for _ in range(M):
    if read() in words:
        cnt += 1

print(cnt)
