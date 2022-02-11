def make_prefix(_list, size, result, mode=1):
    prefix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(i, size):
            if j == i:
                prefix[j][j] = _list[j]
            else:
                prefix[i][j] = prefix[i][j - 1] + _list[j]
            if mode:
                result[prefix[i][j]] = result.get(prefix[i][j], 0) + 1
            else:
                cnt[0] += prefix_A.get(T - prefix[i][j], 0)


T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

prefix_A = {}
make_prefix(A, n, prefix_A)
set_A = sorted([k for k in prefix_A.keys()])
cnt = [0]
make_prefix(B, m, {}, 0)

print(cnt[0])
