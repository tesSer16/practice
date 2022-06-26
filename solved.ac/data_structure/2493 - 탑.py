N = int(input())
arr = list(map(int, input().split()))

stack = [N - 1]
result = [0] * N
for i in range(N - 2, -1, -1):
    a = arr[i]
    while stack and arr[stack[-1]] < a:
        j = stack.pop()
        result[j] = i + 1
    stack.append(i)

print(*result)
