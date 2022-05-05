import sys
read = sys.stdin.readline

for _ in range(int(read())):
    data = input()
    last_one = -1
    idx = 0
    while idx < len(data):
        if data[idx] == '0':
            break
        if data[idx] == '1':
            last_one = idx
        idx += 1

    if last_one == -1:
        if idx == 0:
            print(1)
        elif idx < len(data):
            print(idx + 1)
        else:
            print(idx)
    elif idx == len(data):
        if last_one < idx - 1:
            print(idx - last_one)
        else:
            print(1)
    else:
        print(idx - last_one + 1)

