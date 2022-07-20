from collections import deque


N = int(input())
arr = deque([(v, i + 1) for i, v in enumerate(map(int, input().split()))])
for _ in range(N):
    a, b = arr.popleft()
    arr.rotate(-a + 1 if a > 0 else -a)
    print(b, end=" ")
