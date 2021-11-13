import random


def solution(x1, y1, x2, y2, x3, y3, x4, y4):
    def check(r1, r2, target):
        r = sorted([r1, r2])
        return r[0] <= target <= r[1]

    a, b, c, d, e, f = y4 - y3, x3 - x4, y2 - y1, x1 - x2, (y4 - y3) * x3 - y3 * (x4 - x3), (y2 - y1) * x1 - y1 * (
            x2 - x1)
    det = a * d - b * c
    x, y = d * e - b * f, a * f - e * c

    return_list = []
    if det == 0:
        if a == b == 0:
            if c * (x3 - x1) == - d * (y3 - y1) and all(check(r, s, t) for r, s, t in [(x1, x2, x3), (y1, y2, y3)]):
                return_list.append(1)
                return_list.append((x3, y3))
        elif c == d == 0:
            if a * (x1 - x3) == - b * (y1 - y3) and all(check(r, s, t) for r, s, t in [(x3, x4, x1), (y3, y4, y1)]):
                return_list.append(1)
                return_list.append((x1, y1))

        elif a * (x3 - x1) == - b * (y3 - y1):
            if x1 == x3:
                s1, s2, s3, s4 = y1, y2, y3, y4
            else:
                s1, s2, s3, s4 = x1, x2, x3, x4
            t1, t2 = sorted([(s1, 0), (s2, 1)])
            t3, t4 = sorted([(s3, 2), (s4, 3)])
            if (t1[0] <= t3[0] <= t2[0]) or (t1[0] <= t4[0] <= t2[0]) or (t3[0] <= t2[0] <= t4[0]) or (
                    t3[0] <= t1[0] <= t4[0]):
                return_list.append(1)
                points = [(x1, y2), (x2, y2), (x3, y3), (x4, y4)]
                if t2[0] == t3[0]:
                    return_list.append(points[t2[1]])
                elif t1[0] == t4[0]:
                    return_list.append(points[t1[1]])

    elif all(check(r * det, s * det, t) for r, s, t in [(x1, x2, x), (x3, x4, x), (y1, y2, y), (y3, y4, y)]):
        return_list.append(1)
        return_list.append((x / det, y / det))

    return return_list if return_list else [0]


def other(x1, y1, x2, y2, x3, y3, x4, y4):
    point = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]

    def check(a, b, c, d):
        if ccw(a, b, c) * ccw(a, b, d) == 0:
            if ccw(c, d, a) * ccw(c, d, b) == 0:
                if a > b:
                    a, b = b, a
                if c > d:
                    c, d = d, c
                if b >= c and a <= d:
                    return True
                else:
                    return False
        if ccw(a, b, c) * ccw(a, b, d) <= 0:
            if ccw(c, d, a) * ccw(c, d, b) <= 0:
                return True
        return False

    def ccw(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])

    return_list = []
    if check(point[0], point[1], point[2], point[3]):
        return_list.append(1)
        try:
            x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
                        (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
            y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
                        (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
            return_list.append((x, y))
        except ZeroDivisionError:
            if point[0] > point[1]:
                point[0], point[1] = point[1], point[0]
            if point[2] > point[3]:
                point[2], point[3] = point[3], point[2]
            if point[1] == point[2]:
                return_list.append((point[1][0], point[1][1]))
            elif point[0] == point[3]:
                return_list.append((point[0][0], point[0][1]))
    else:
        return_list.append(0)

    return return_list


for _ in range(10000):
    case = [random.randint(-5, 5) for _ in range(8)]
    v1, v2 = solution(*case), other(*case)
    if v1 != v2:
        print(case)
        print(v1)
        print(v2)
        print()
