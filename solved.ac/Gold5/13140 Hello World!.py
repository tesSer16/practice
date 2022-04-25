def dfs(selected, k):
    if len(selected) == 7:
        d, e, h, l, o, r, w = selected
        val1 = h * 10 ** 4 + e * 10 ** 3 + l * 110 + o
        val2 = w * 10 ** 4 + o * 10 ** 3 + r * 10 ** 2 + l * 10 + d
        if val1 + val2 == N:
            print(f"  {val1}")
            print(f"+ {val2}")
            print(f"-------")
            print(f"{N:7}")
            exit(0)
        return

    for i in range(10):
        if not i and (len(selected) in [2, 6]):
            continue

        if not k & (1 << i):
            dfs(selected + [i], k | (1 << i))


N = int(input())

dfs([], 0)
print("No Answer")
