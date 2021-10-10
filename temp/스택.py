stack = []
cnt = 0
commands = {
            "push": (lambda x: stack.append(x)),
            "pop": (lambda: print(stack.pop()) if stack else print(-1)),
            "size": (lambda: print(cnt)),
            "empty": (lambda: print(0) if stack else print(1)),
            "top": (lambda: print(stack[-1]) if stack else print(-1))
           }

for _ in ' ' * int(input()):
    cmd = input().split()
    commands[cmd[0]](cmd[1]) if len(cmd) == 2 else commands[cmd[0]]()
