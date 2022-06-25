N = int(input())
arr = list(map(int, input().split()))

stack = [(arr[0], 0)]
result = [-1] * N
for i in range(1, N):
    print(stack)
    a = arr[i]
    while stack and stack[-1][0] < a:
        b, j = stack.pop()
        result[j] = a
    stack.append((a, i))

print(*result)
