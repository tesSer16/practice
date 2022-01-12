def test(_list, d):
    if d == 2:
        return
    print(_list)
    _list[0] = d ** 2
    print(_list)
    test(_list[::], d + 1)
    print(_list)


a = [3]
test(a[::], 0)
print(a)
