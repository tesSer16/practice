from collections import deque
import sys

for _ in range(int(input())):
    n = int(sys.stdin.readline())

    q = deque([[n, 0]])
    while q:
        num, cnt = q.popleft()
        if num % 25 == 0:
            print(cnt)
            break

        str_num = str(num)
        if len(str_num) == 1:
            continue
        for i in range(len(str_num)):
            q.append([int(str_num[:i] + str_num[i + 1:]), cnt + 1])
