import random


def my(x1, y1, x2, y2, x3, y3, x4, y4):
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
                return 1
        elif c == d == 0:
            if a * (x1 - x3) == - b * (y1 - y3) and all(check(r, s, t) for r, s, t in [(x3, x4, x1), (y3, y4, y1)]):
                return 1

        elif a * (x3 - x1) == - b * (y3 - y1):
            if x1 == x3:
                x1, x2, x3, x4 = y1, y2, y3, y4
            t1, t2 = sorted([x1, x2])
            t3, t4 = sorted([x3, x4])
            if (t1 <= t3 <= t2) or (t1 <= t4 <= t2) or (t3 <= t2 <= t4) or (t3 <= t1 <= t4):
                return 1

    elif all(check(r * det, s * det, t) for r, s, t in [(x1, x2, x), (x3, x4, x), (y1, y2, y), (y3, y4, y)]):
        return 1

    return 0


def other(x1, y1, x2, y2, x3, y3, x4, y4):
    point = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]

    def ccw(p1, p2, p3):
        return (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1])

    def checkCross(p1, p2, p3, p4):
        is_result = False
        result = 0
        p123 = ccw(p1, p2, p3)
        p124 = ccw(p1, p2, p4)
        p341 = ccw(p3, p4, p1)
        p342 = ccw(p3, p4, p2)

        if p123 * p124 == 0 and p341 * p342 == 0:
            is_result = True
            if min(p1[0], p2[0]) <= max(p3[0], p4[0]) and min(p3[0], p4[0]) <= max(p1[0], p2[0]) and min(p1[1],
                                                                                                         p2[1]) <= max(
                p3[1], p4[1]) and min(p3[1], p4[1]) <= max(p1[1], p2[1]):
                result = 1

        if p123 * p124 <= 0 and p341 * p342 <= 0:
            if not is_result:
                result = 1

        return result

    return checkCross(point[0], point[1], point[2], point[3])


for _ in range(100000):
    _list = [random.randint(-5, 5) for _ in range(8)]
    v1, v2 = my(*_list), other(*_list)
    if v1 != v2:
        print(_list, v1, v2)
