import sys
read = sys.stdin.readline

for _ in range(int(read())):
    stack1 = []
    stack2 = []
    for s in read().strip():
        if s == '<' and stack1:
            stack2.append(stack1.pop())
        elif s == '>' and stack2:
            stack1.append(stack2.pop())
        elif s == '-' and stack1:
            stack1.pop()
        elif s not in "<>-":
            stack1.append(s)

    print(''.join(stack1) + ''.join(stack2[::-1]))
