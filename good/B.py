import sys
read = sys.stdin.readline


for _ in range(int(read())):
    N = int(read())
    if N % 3 == 2 or N % 9 == 0:
        print('TAK')
    else:
        print("NIE")
