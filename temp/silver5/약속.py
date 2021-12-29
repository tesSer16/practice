import sys
input = sys.stdin.readline

N = int(input())
SmA = sorted([(lambda x, y: x - y)(*map(int, input().split())) for _ in range(N)])

if N % 2 == 0:
    print(abs(SmA[N//2] - SmA[N//2 - 1]) + 1)
else:
    print(1)
