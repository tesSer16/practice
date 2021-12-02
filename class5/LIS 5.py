import bisect

N = int(input())
arr = list(map(int, input().split()))
LIS = [arr[0]]
bt = [0] * N
idx = 0
for i in range(1, N):
    if arr[i] > LIS[idx]:
        LIS.append(arr[i])
        idx += 1
        bt[i] = idx
    else:
        bt[i] = bisect.bisect_left(LIS, arr[i])
        LIS[bt[i]] = arr[i]


max_idx, ans = idx + 1, []
for i in range(N - 1, -1, -1):
    if bt[i] == max_idx - 1:
        max_idx = bt[i]
        ans.append(arr[i])

print(idx + 1)
print(*ans[::-1])
