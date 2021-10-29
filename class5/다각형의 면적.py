import sys


def tri_area(p1, p2, p3):
    v1 = (p2[0] - p1[0], p2[1] - p1[1])
    v2 = (p3[0] - p1[0], p3[1] - p1[1])
    return v1[0] * v2[1] - v1[1] * v2[0]


area = 0
N = int(input())
origin = tuple(map(int, input().split()))
second = tuple(map(int, input().split()))
for _ in range(N - 2):
    third = tuple(map(int, sys.stdin.readline().split()))
    area += tri_area(origin, second, third)
    second = third

print(abs(area) / 2)
