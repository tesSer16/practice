import sys
read = sys.stdin.readline
for _ in range(int(read())):
    n = int(read())
    arr = list(read().strip())
    m = arr.count('1')
    result = []
    for i in range(n):
        if arr[i] == '1' and i < n - m:
            result.append(i + 1)
        elif arr[i] == '0' and i >= n - m:
            result.append(i + 1)
    if result:
        print(1)
        print(len(result), *result)
    else:
        print(0)
