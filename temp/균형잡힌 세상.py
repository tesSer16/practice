while True:
    string = input()
    stack = [None]
    if string == '.':
        break

    yes = True
    for s in string:
        if s in "([":
            stack.append(s)
        elif s == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                yes = False
                break
        elif s == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                yes = False
                break

    if yes and stack == [None]:
        print("yes")
    else:
        print("no")
