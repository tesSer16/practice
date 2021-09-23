def judge(num):
    n = 0
    while num % 5 == 0:
        n += 1
        num //= 5
    
    return n


N = int(input())
result = 0
for i in range(5, N + 1, 5):
    result += judge(i)

print(result)
