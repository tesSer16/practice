cnt = 0
for _ in range(int(input())):
    string = input()
    stack = []
    for s in string:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)

    if not stack:
        cnt += 1

print(cnt)
