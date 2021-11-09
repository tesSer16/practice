import sys
read = sys.stdin.readline

for _ in range(int(input())):
    n = int(read())
    sorted_data = sorted([(k, v) for k, v in zip(map(int, read().split()), read().strip())], key=lambda x: (x[1], x[0]))

    result = "Yes"
    for t in range(1, n + 1):
        data = sorted_data[t - 1]
        if data[1] == 'B':
            if data[0] < t:
                result = "No"
                break
        else:
            if data[0] > t:
                result = "No"
                break

    print(result)
