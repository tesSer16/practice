import sys
read = sys.stdin.readline

for _ in range(int(read())):
    n = read().strip()
    if int(n[-1]) % 2 == 0:
        print(0)
    elif int(n[0]) % 2 == 0:
        print(1)
    else:
        for num in n:
            if int(num) % 2 == 0:
                print(2)
                break
        else:
            print(-1)
