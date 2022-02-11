import sys

stack = [None]
N = int(input())
seq = [int(sys.stdin.readline()) for _ in ' ' * N]

n = 1
finished = False
answer = []
for s in seq:
    while stack[-1] != s:
        if n > N:
            finished = True
            break

        answer.append('+')
        stack.append(n)
        n += 1
    answer.append('-')
    stack.pop()

    if finished:
        break

if finished:
    print("NO")
else:
    print(*answer, sep='\n')
