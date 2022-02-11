import sys


def plus_ultra(st, num):
    result = []
    factor = 3 * 2 ** num
    for s in st:
        result.append(' ' * factor + s + ' ' * factor)
    for s in st:
        result.append(s + ' ' + s)

    return result


star = ["  *  ",
        " * * ",
        "*****"]

k = -1
N = int(input()) // 3
while N:
    N //= 2
    k += 1

for i in range(k):
    star = plus_ultra(star, i)

for line in star:
    sys.stdout.write(line + '\n')
