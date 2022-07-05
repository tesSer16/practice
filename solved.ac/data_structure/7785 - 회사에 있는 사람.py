import sys
read = sys.stdin.readline

_set = set()
for _ in range(int(read())):
    name, state = read().strip().split()
    if state == "enter":
        _set.add(name)
    else:
        _set.remove(name)

print(*sorted(list(_set), reverse=True))
