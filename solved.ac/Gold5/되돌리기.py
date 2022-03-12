_list = []
text = ""
for _ in range(int(input())):
    mode, c, t = input().split()
    if mode == "type":
        text += c

    else:
        target = int(t) - int(c)
        for i in range(len(_list) - 1, -1, -1):
            if target > _list[i][0]:
                text = _list[i][1]
                break
        else:
            text = ""

    _list.append((int(t), text))

print(text)
