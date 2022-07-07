input()
result = []
for i, a in enumerate(map(int, input().split())):
    result.insert(a, i + 1)

print(*result[::-1])
