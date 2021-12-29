import math


def dist(x, y, z, w):
    return math.sqrt((x - z)**2 + (y - w)**2)


x1, y1, x2, y2, x3, y3 = map(int, input().split())
a, b, c = dist(x2, y2, x3, y3), dist(x1, y1, x3, y3), dist(x1, y1, x2, y2)

if x1 == x2 == x3 or y1 == y2 == y3:
    print(-1)
elif (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2):
    print(-1)
else:
    temp = [a + b, b + c, a + c]
    print(2 * (max(temp) - min(temp)))
