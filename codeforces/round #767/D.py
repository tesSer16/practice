import sys
read = sys.stdin.readline


def check(arr):
    check2 = [[0] * 26 for _ in range(26)]
    check3 = [[[0] * 26 for _ in range(26)] for _ in range(26)]
    for i in range(n):
        if arr[i] == arr[i][::-1]:
            return True
        if len(arr[i]) == 2:
            a, b = arr[i]
            check2[ord(a) - 97][ord(b) - 97] = 1
            if check2[ord(b) - 97][ord(a) - 97]:
                return True
        else:
            a, b, c = arr[i]
            check2[ord(a) - 97][ord(b) - 97] = 1
            check2[ord(b) - 97][ord(c) - 97] = 1
            check3[ord(a) - 97][ord(b) - 97][ord(c) - 97] = 1
            if check2[ord(c) - 97][ord(b) - 97] or check3[ord(c) - 97][ord(b) - 97][ord(a) - 97]:
                return True

    return False


for _ in range(int(read())):
    n = int(read())
    print("YES" if check([read().strip() for _ in range(n)]) else "NO")
