def judge(k, num):
    result = 0
    while num != 0:
        num //= k
        result += num       

    return result
        

n, m = map(int, input().split())
print(min(judge(2, n) - judge(2, n-m) - judge(2, m),
          judge(5, n) - judge(5, n-m) - judge(5, m)))
