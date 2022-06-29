stack = []
flag = False
for s in input():
    if s == '<':
        flag = True
        if stack:
            print(''.join(stack[::-1]), end="")
            stack = []
    elif s == '>':
        print('<' + ''.join(stack) + '>', end="")
        stack = []
        flag = False
    elif s == ' ' and not flag:
        print(''.join(stack[::-1]), end=" ")
        stack = []
    else:
        stack.append(s)

if stack:
    print(''.join(stack[::-1]))
