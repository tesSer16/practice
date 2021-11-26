import sys
read = sys.stdin.readline

for _ in range(int(read())):
    n, s = map(int, read().split())
    arr = list(map(int, read().split()))
    answer = []
    _sum = s
    stack = []
    for i in range(n):
        print(stack)
        if _sum + arr[i] < 0:
            if len(answer) < len(stack):
                answer = stack[::]
            stack.clear()
            _sum = s
        else:
            _sum += arr[i]
            stack.append(i + 1)
    if len(answer) < len(stack):
        answer = stack[::]

    if answer:
        print(*answer)
    else:
        print(-1)
    print()
