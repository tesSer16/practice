import sys
read = sys.stdin.readline
for _ in range(int(read())):
    n = int(read())
    string = read().strip()
    min_diff = n
    try:
        last_a = string.index('a')
    except ValueError:
        last_a = n - 1

    b = c = 0
    for i in range(last_a + 1, n):
        if string[i] == 'a':
            if i - last_a > 3 or max(b, c) >= 2:
                pass
            elif i - last_a < min_diff:
                min_diff = i - last_a
            if min_diff == 1:
                break
            last_a = i
            b = c = 0
        elif string[i] == 'b':
            b += 1
        elif string[i] == 'c':
            c += 1

    if min_diff == n:
        print(-1)
    else:
        print(min_diff + 1)
