import sys
read = sys.stdin.readline


for _ in range(int(read())):
    n = int(read())
    a = [*map(int, read().split())]
    s = set()
    cnt = 0
    M = max(a)
    b = []
    for i in range(n):
        if a[i] not in s:
            s.add(a[i])
            cnt += 1
        # print(s)
        if M + 1 == cnt and a[i] in s:
            b.append(cnt)
            s.clear()
            cnt = 0
            M = max(a[i:])
    if s:
        for i in range(M):
            if i not in s:
                b.append(i)
                break

    print(len(b))
    print(*b)
