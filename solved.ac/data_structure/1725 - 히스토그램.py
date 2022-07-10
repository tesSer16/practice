import sys
read = sys.stdin.readline

N = int(read())
arr = [int(read()) for _ in range(N)]
result = 0
stack = []
for i in range(N):
    while stack and arr[stack[-1]] >= arr[i]:
        h = arr[stack.pop()]
        w = i - 1 - stack[-1] if stack else i
        result = max(result, h * w)
    stack.append(i)

while stack:
    h = arr[stack.pop()]
    w = N - 1 - stack[-1] if stack else N
    result = max(result, h * w)

print(result)
