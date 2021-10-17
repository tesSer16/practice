import sys
for _ in range(int(input())):
    a, b, c = map(int, sys.stdin.readline().split())
    if c > a:
        print("No")
        continue

    if b % 2 == 0:
        if (a - c) % 2 == 0:
            print("Yes")
        else:
            print("No")
    else:
        if a >= c >= 1 and (a - c) % 2 == 0:
            print("Yes")
        else:
            if c:
                if (a - c) % 2 == 0:
                    print("Yes")
                else:
                    print("No")
            else:
                if a >= 2 and a % 2 == 0:
                    print("Yes")
                else:
                    print("No")
