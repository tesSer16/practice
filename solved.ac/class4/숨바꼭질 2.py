N, K = map(int, input().split())
MAX = 100001
visited = [MAX] * MAX
visited[N] = 0
q = [N]

finished = False
cnt, d = 0, 0
while q:
    temp = []
    for current in q:
        if current == K:
            print(d)
            print(q.count(K))
            break

        for i, next_x in enumerate([current * 2, current - 1, current + 1]):
            if 0 <= next_x < MAX and d <= visited[next_x]:
                visited[next_x] = d
                temp.append(next_x)

    q = temp[::] if not finished else []
    d += 1
