import sys
from itertools import permutations


def gcd(a, b):
    pass


N = int(input())
S = [sys.stdin.readline().rstrip() for _ in range(N)]
K = int(input())

answer = 0
per = list(permutations(S))
len_per = len(per)
for p in per:
    if int(''.join(p)) % K == 0:
        answer += 1

if answer == 0:
    print("1/0")
else:
    print(answer, len_per)
