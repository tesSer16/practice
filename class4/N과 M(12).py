def job(_list=[], i=0, d=0):
    if d == M:
        print(*_list)
        return

    for j in range(i, N):
        job(_list + [num_list[j]], j, d + 1)


dum, M = map(int, input().split())
num_list = sorted(set(map(int, input().split())))
N = len(num_list)
job()
