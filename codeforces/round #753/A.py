for _ in range(int(input())):
    keyboard = {k: i for i, k in enumerate(input())}
    string = input()
    _sum = 0
    for i in range(len(string) - 1):
        _sum += abs(keyboard[string[i]] - keyboard[string[i + 1]])

    print(_sum)
