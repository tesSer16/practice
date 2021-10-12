import sys
from collections import deque

input = sys.stdin.readline
for _ in range(int(input())):
    functions = input().strip()
    n = int(input())
    num_list = input()
    num_deq = deque(list((num_list[1:-2]).split(',')) if n else [])
    left = 1
    try:
        for f in functions:
            if f == 'D':
                num_deq.popleft() if left else num_deq.pop()
            else:
                left ^= 1

        if num_deq:
            if not left:
                num_deq = reversed(num_deq)
            print("[" + ','.join(num_deq) + "]")
        else:
            print("[]")

    except IndexError:
        print("error")
