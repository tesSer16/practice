import bisect

_list = []
text = ""
for _ in range(int(input())):
    mode, c, t = input().split()
    if mode == "type":
        text += c

    else:
        target = int(t) - int(c)
        idx = bisect.bisect_left(_list, (target, ''))
        if idx:
            text = _list[idx - 1][1]
        else:
            text = ""

    _list.append((int(t), text))

print(text)
