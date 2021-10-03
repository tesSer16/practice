def solve(num, cnt):
    global result
    for a in range(int(num**0.5), int((num//(4 - cnt + 1))**0.5), -1):
        if num == a*a:
            result = min(cnt, result)
        else:
            solve(num - a*a, cnt + 1)


n = int(input())
result = 4
solve(n, 1)
print(result)
