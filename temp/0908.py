def f(num, d):
    if d == 7:
        if num % 27 == 0:
            result.append(num)
        return
    for i in [3, 6, 9]:
        f(num * 10 + i, d + 1)


result = []
f(0, 1)


print(len(result))
print(result)
    
