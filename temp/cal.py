last_day = int(input())
ini_day = int(input())

print((ini_day - 1) * '   ', end="")
for i in range(ini_day, last_day + ini_day):
    print("%2d " % (i - ini_day + 1), end="")
    if i % 7 == 0:
        print()
