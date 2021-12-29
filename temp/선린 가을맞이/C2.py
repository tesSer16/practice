import sys

M, N = map(int, input().split())
stacks = []
able = True
for _ in range(N):
    n = int(input())
    temp = list(map(int, sys.stdin.readline().split()))
    for i in range(n - 1):
        if temp[i] < temp[i + 1]:
            able = False
            break

    if not able:
        break

if able:
    print("Yes")
else:
    print("No")
