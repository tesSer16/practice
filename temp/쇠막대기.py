cnt = 0
stack = []
last = ""
result = 0
for s in input():
    # print(stack, result, cnt, last)
    if len(s) == 0:
        stack.append(s)
        last = s
        continue

    if s == ')' and last == '(':
        cnt -= 1
        result += cnt - 1
        stack.pop()
    elif s == ')' and stack[-1] == '(':
        stack.pop()
        cnt -= 1
    elif s == '(':
        cnt += 1
        result += 1
        stack.append('(')

    last = s

print(result)
