from collections import Counter

for _ in range(int(input())):
    input()
    arr = [*map(int, input().split())]
    ans = set(arr)
    counter = Counter(arr)
    for c in counter:
        if c and counter[c] >= 2 and -c not in ans:
            ans.add(-c)
    print(len(ans))
