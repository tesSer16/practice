import sys
read = sys.stdin.readline

for _ in range(int(read())):
    n, k = map(int, read().split())
    mice = sorted(list(map(int, read().split())))
    cat = 0
    cnt = 0
    while mice:
        save = mice.pop()
        if save > cat:
            cat += n - save
            cnt += 1
        else:
            break

    print(cnt)
