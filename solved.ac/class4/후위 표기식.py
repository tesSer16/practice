def nest(str_list):
    result = []
    stack = []
    temp = []
    for s in str_list:
        if s == "(":
            if stack:
                temp.append("(")
            stack.append("(")
        elif stack:
            if s == ")" and stack[-1] == "(":
                stack.pop()
                if stack:
                    temp.append(")")
                    continue
                t = nest(temp)
                result.append(t)
                temp.clear()
            else:
                temp.append(s)
        else:
            result.append(s)

    return add_bracket(result)


def add_bracket(str_list):
    result = str_list[::]
    while True:
        for i in range(0, len(result) - 1, 2):
            if result[i + 1] == "*" or result[i + 1] == "/":
                result = result[:i] + [result[i:i + 3]] + result[i + 3:]
                break
        else:
            break

    while True:
        for i in range(0, len(result) - 1, 2):
            if result[i + 1] == "+" or result[i + 1] == "-":
                result = result[:i] + [result[i:i + 3]] + result[i + 3:]
                break
        else:
            break

    return result[0]


def postfix_notation(a, op, b):
    if isinstance(a, str):
        print(a, end="")
    else:
        postfix_notation(*a)

    if isinstance(b, str):
        print(b, end="")
    else:
        postfix_notation(*b)

    print(op, end="")


eq = nest(list(input()))
if len(eq) == 1:
    print(eq[0])
else:
    postfix_notation(*eq)
