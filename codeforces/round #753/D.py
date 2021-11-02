import sys
read = sys.stdin.readline

for _ in range(int(input())):
    n = int(read())
    nums = list(map(int, read().split()))
    commands = read().strip()
    sorted_data = sorted([(k, v) for k, v in zip(nums, commands)], key=lambda x: (x[1], x[0]))

    check = [0] * n
    i = n - 1
    while sorted_data[i][1] != 'B':
        num = sorted_data[i][0]
        bound = num if num > 0 else 1
        for nu in range(n, bound - 1, -1):
            if not check[nu - 1]:
                check[nu - 1] = 1
                break

        i -= 1
        if i == -1:
            break

    for j in range(i + 1):
        num = sorted_data[j][0]
        bound = num + 1 if num < n else n + 1
        for nu in range(1, bound):
            if not check[nu - 1]:
                check[nu - 1] = 1
                break

    if all(check):
        print("YES")
    else:
        print("NO")
