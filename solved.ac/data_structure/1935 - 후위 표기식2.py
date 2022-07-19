N = int(input())
string = input()
data = {chr(65 + i): input() for i in range(N)}

stack = []
for s in string:
    if s in "*+/-":
        b, a = stack.pop(), stack.pop()
        stack.append(str(eval(a + s + b)))
    else:
        stack.append(data[s])

print(f"{float(stack[0]):.2F}")
