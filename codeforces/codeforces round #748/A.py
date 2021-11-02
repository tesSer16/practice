t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    k = max(nums)
    maxs = []
    for i in range(3):
        if nums[i] == k:
            maxs.append(nums[i])

    for i in range(3):
        if nums[i] not in maxs:
            print(k - nums[i] + 1, end=' ')
        else:
            if len(maxs) == 1:
                print(0, end=' ')
            else:
                print(1, end=' ')

    print()
