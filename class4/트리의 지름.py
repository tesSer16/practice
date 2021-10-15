import sys
sys.setrecursionlimit(10**6)


def dfs(v, tot_dist, visited):
    for w, dist in data_dic[v]:
        if max_dist[w] and len(data_dic[v]) == 1:
            max_dist[v] = dist + max_dist[w]
            ans[0] = max(max_dist[v], ans[0])
            return

        if not visited.get(w, 0):
            visited[w] = 1
            dfs(w, tot_dist + dist, visited)
            del visited[w]

    max_dist[v] = max(max_dist[v], tot_dist)
    ans[0] = max(max_dist[v], ans[0])


V = int(input())
max_dist = [0 for _ in range(V + 1)]
ans = [-float('inf')]
data_dic = {}
for _ in range(V):
    node, *data, dum = map(int, sys.stdin.readline().split())
    for i in range(0, len(data), 2):
        data_dic[node] = data_dic.get(node, []) + [(data[i], data[i + 1])]

for vi in range(1, V + 1):
    dfs(vi, 0, {vi: 1})

print(ans[0])
