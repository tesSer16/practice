def check(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return check(20, 20, 20)
    
    if not w[a][b][c]:
        if a < b < c:
            w[a][b][c] = check(a, b, c-1) + check(a, b-1, c-1) - check(a, b-1, c)
        else:
            w[a][b][c] = check(a-1, b, c) + check(a-1, b-1, c) + check(a-1, b, c-1) - check(a-1, b-1, c-1)

    return w[a][b][c]


w = [[[0] * 21 for _ in range(21)] for _ in range(21)]
while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    
    print("w(%d, %d, %d) = " % (a, b, c), check(a, b, c))
