import sys

M, N = map(int, input().split())
stacks = []
for _ in range(N):
    n = int(input())
    stacks.append(list(map(int, sys.stdin.readline().split())))

i = 1
able = True
while i != M:
    for stack in stacks:
        if stack and stack[-1] == i:
            stack.pop()
            i += 1
            break
    else:
        able = False

    if not able:
        break

if i == M:
    print("Yes")
else:
    print("No")
