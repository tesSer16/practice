from collections import deque

N = int(input())
visited = [0] * (N + 1)
q = deque([N])
while q and not visited[1]:
    num = q.popleft()
    for cond, value in zip([not num % 3, not num % 2, 1], [num // 3, num // 2, num - 1]):
        if cond and not visited[value]:
            visited[value] = num
            q.append(value)

n = 1
answer = deque()
while n != N:
    answer.appendleft(n)
    n = visited[n]

print(len(answer))
print(N, *answer)
