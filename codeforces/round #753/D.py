import sys
read = sys.stdin.readline


def dfs(d):
    if result[0]:
        return
    if d == n + 1:
        result[0] = True
        return
    for j in range(n):
        if check[d][j] and not visited[j]:
            visited[j] = 1
            dfs(d + 1)
            visited[j] = 0


for _ in range(int(input())):
    n = int(read())
    nums = list(map(int, read().split()))
    commands = read().strip()
    check = [[0] * n for _ in range(n + 1)]
    for i in range(n):
        if commands[i] == 'R':
            bound = nums[i] if nums[i] > 0 else 1
            for nu in range(bound, n + 1):
                check[nu][i] = 1
        else:
            if nums[i] <= 0:
                continue
            else:
                bound = nums[i] + 1 if nums[i] < n else n + 1
                for nu in range(1, bound):
                    check[nu][i] = 1

    visited = [0] * n
    result = [False]
    dfs(1)
    if result[0]:
        print("YES")
    else:
        print("NO")
