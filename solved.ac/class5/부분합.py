N, S = map(int, input().split())
num_list = list(map(int, input().split()))
prefix_sum = [0] * (N + 1)
for k in range(1, N + 1):
    prefix_sum[k] += prefix_sum[k - 1] + num_list[k - 1]

length = 1000001
left, right = 0, 1
while left < N:
    if prefix_sum[right] - prefix_sum[left] >= S:
        length = min(length, right - left)
        left += 1
    else:
        if right < N:
            right += 1
        else:
            left += 1

print(length if length < 1000001 else 0)
