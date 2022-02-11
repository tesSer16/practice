string = list(input())
explode = list(input())
n = len(explode)
stack = []
cnt = 0

if n > 1:
    for s in string:
        if cnt >= n - 1 and stack[-(n - 1):] + [s] == explode:
            for _ in range(n - 1):
                stack.pop()
                cnt -= 1
        else:
            stack.append(s)
            cnt += 1

    print(''.join(stack) if stack else "FRULA")
else:
    result = ''.join(string).replace(explode[0], '')
    print(result if result else "FRULA")
