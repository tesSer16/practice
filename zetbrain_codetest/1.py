queries = [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]
m = 5
n = 2
x = 0
y = 1


def check(r, c):
    for q in queries:
        if q[0] == 0:
            if c - q[1] <= 0:
                c = 0
            else:
                c -= q[1]
        elif q[0] == 1:
            if c + q[1] >= m - 1:
                c = n - 1
            else:
                c += q[1]
        elif q[0] == 2:
            if r - q[1] <= 0:
                r = 0
            else:
                r -= q[1]
        else:
            if r + q[1] >= n - 1:
                r = n - 1
            else:
                r += q[1]

        print(r, c)

    if (x, y) == (r, c):
        return True


print(check(0, 1))
