N, M = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0, max(nums)
while start + 1 < end:
    mid = (start + end) // 2

    tot_length = 0
    for n in nums:
        tot_length += max(0, n - mid)

    if tot_length >= M:
        start = mid
    else:
        end = mid

print(start)
