for _ in range(int(input())):
    n = int(input())
    dic = {}

    for _ in range(n):
        name, var = input().split()

        if var in dic:
            dic[var] += 1
        else:
            dic[var] = 1

    result = 1
    for v in dic.values():
        result *= (v + 1)
    print(result - 1)
