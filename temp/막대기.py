def div2(num):
    global result
    if num < 2:
        result += num
        return
    div2(num // 2)
    result += num % 2


N = int(input())
result = 0
div2(N)
print(result)
