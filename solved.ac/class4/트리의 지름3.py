import sys
sys.setrecursionlimit(100001)


def dfs(v, tot_dist, last_v):
    if tot_dist > ans[0]:
        ans[0] = tot_dist
        ans[1] = v

    for w, d in data_list[v]:
        if w != last_v:
            dfs(w, tot_dist + d, v)


n = int(input())
ans = [0, -1]
data_list = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    node1, node2, dist = map(int, sys.stdin.readline().split())
    data_list[node1].append([node2, dist])
    data_list[node2].append([node1, dist])

dfs(1, 0, 0)
dfs(ans[1], 0, 0)

print(ans[0])
