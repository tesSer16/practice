import bisect
import sys

read = sys.stdin.readline

n = int(read())
arr = sorted(tuple(map(int, read().split())) for _ in range(n))
seq = [arr[0][1]]
bt = [0] * n
idx = 0
for i in range(1, n):
    if arr[i][1] > seq[idx]:
        seq.append(arr[i][1])
        idx += 1
        bt[i] = idx
    else:
        bt[i] = bisect.bisect_left(seq, arr[i][1])
        seq[bt[i]] = arr[i][1]

max_idx, ans = max(bt) + 1, []
for i in range(n - 1, -1, -1):
    if bt[i] == max_idx - 1:
        max_idx = bt[i]
    else:
        ans.append(arr[i][0])

print(len(ans))
print(*ans[::-1], sep='\n')
