def solution(x1, y1, x2, y2, x3, y3, x4, y4):
    def check(r1, r2, target):
        r = sorted([r1, r2])
        return r[0] <= target <= r[1]

    a, b, c, d, e, f = y4 - y3, x3 - x4, y2 - y1, x1 - x2, (y4 - y3) * x3 - y3 * (x4 - x3), (y2 - y1) * x1 - y1 * (
            x2 - x1)
    det = a * d - b * c
    x, y = d * e - b * f, a * f - e * c

    if det == 0:
        if a == b == 0:
            if c * (x3 - x1) == - d * (y3 - y1) and all(check(r, s, t) for r, s, t in [(x1, x2, x3), (y1, y2, y3)]):
                print(1)
                print(x3, y3)
                return
        elif c == d == 0:
            if a * (x1 - x3) == - b * (y1 - y3) and all(check(r, s, t) for r, s, t in [(x3, x4, x1), (y3, y4, y1)]):
                print(1)
                print(x1, y1)
                return

        elif a * (x3 - x1) == - b * (y3 - y1):
            if x1 == x2:
                s1, s2, s3, s4 = y1, y2, y3, y4
            else:
                s1, s2, s3, s4 = x1, x2, x3, x4
            t1, t2 = sorted([(s1, 0), (s2, 1)])
            t3, t4 = sorted([(s3, 2), (s4, 3)])
            if (t1[0] <= t3[0] <= t2[0]) or (t1[0] <= t4[0] <= t2[0]) or (t3[0] <= t2[0] <= t4[0]) or (
                    t3[0] <= t1[0] <= t4[0]):
                print(1)
                points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
                if t2[0] == t3[0]:
                    print(*points[t2[1]])
                elif t1[0] == t4[0]:
                    print(*points[t1[1]])
                return

    elif all(check(r * det, s * det, t) for r, s, t in [(x1, x2, x), (x3, x4, x), (y1, y2, y), (y3, y4, y)]):
        print(1)
        print(x / det, y / det)
        return

    print(0)


solution(*map(int, input().split()), *map(int, input().split()))
