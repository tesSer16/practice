import sys
sys.setrecursionlimit(100001)


def dfs(v, tot_dist, last_v):
    if tot_dist > ans[0]:
        ans[0] = tot_dist
        ans[1] = v

    for w, dist in data_list[v]:
        if w != last_v:
            dfs(w, tot_dist + dist, v)


V = int(input())
ans = [0, -1]
data_list = [[] for _ in range(V + 1)]
for _ in range(V):
    node, *data, dum = map(int, sys.stdin.readline().split())
    for i in range(0, len(data), 2):
        data_list[node].append([data[i], data[i + 1]])

dfs(1, 0, 0)
dfs(ans[1], 0, 0)

print(ans[0])
