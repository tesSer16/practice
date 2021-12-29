import sys
read = sys.stdin.readline

for _ in range(int(read())):
    n = int(read())
    arr = [*map(int, read().split())]
    answer = n
    for a in range(-200, 201):
        for d in range(-400, 401):
            temp = n
            for i in range(n):
                if a / 2 + d / 2 * i == arr[i]:
                    temp -= 1
            answer = min(answer, temp)

    print(answer)
