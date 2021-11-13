import sys
read = sys.stdin.readline


def find(s):
    if "aa" in s:
        return 2
    elif "aca" in s or "aba" in s:
        return 3
    elif "abca" in s or "acba" in s:
        return 4
    elif "abbacca" in s or "accabba" in s:
        return 7
    else:
        return -1


for _ in range(int(read())):
    n = int(read())
    print(find(read().strip()))
