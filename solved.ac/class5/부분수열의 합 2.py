import sys
sys.setrecursionlimit(10**7)


def left(depth, s):
    if depth == mid:
        check[s] = check.get(s, 0) + 1
        return

    left(depth + 1, s)
    left(depth + 1, s + arr[depth])


def right(depth, s):
    global ans
    if depth == N:
        ans += check.get(S - s, 0)
        return

    right(depth + 1, s)
    right(depth + 1, s + arr[depth])


N, S = map(int, input().split())
arr = list(map(int, input().split()))

check = {}
mid = N // 2
ans = 0

left(0, 0)
right(mid, 0)

print(ans if S else ans - 1)
