def pair(a, b):
    return (a, b) in [('(', ')'), ('[', ']')]


def solve(s):
    if not s:
        return 1
    if s == "()":
        return 2
    if s == "[]":
        return 3
    result = 0
    stack = []
    _next = []
    start = s[0]
    j = 1
    while j < len(s):
        if not stack and pair(start, s[j]):
            result += {'(': 2, '[': 3}[start] * solve(''.join(_next))
            _next = []
            j += 1
            if j < len(s) - 1:
                start = s[j]
                j += 1
            continue
        elif stack and pair(stack[-1], s[j]):
            stack.pop()
        else:
            stack.append(s[j])
        _next.append(s[j])
        j += 1

    return result


string = input()
pre_stack = []
for ds in string:
    if pre_stack and pair(pre_stack[-1], ds):
        pre_stack.pop()
    else:
        pre_stack.append(ds)

if pre_stack:
    print(0)
else:
    print(solve(string))
