import sys


S = set()
commands = {"add": S.add,
            "remove": S.remove,
            "check": lambda x: print(1 if x in S else 0),
            "toggle": lambda x: S.remove(x) if x in S else S.add(x),
            "all": lambda: S.update([i for i in range(1, 21)]),
            "empty": S.clear}

for _ in range(int(input())):
    command = list((sys.stdin.readline().strip()).split())
    try:
        if len(command) == 1:
            commands[command[0]]()
        else:
            commands[command[0]](int(command[1]))
    except KeyError:
        pass
