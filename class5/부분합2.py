def solve(x, s):
    _sum = 0
    length = N + 1
    left = 0
    for right in range(N):
        _sum += x[right]
        while _sum >= s and left <= right:
            length = min(length, right - left + 1)
            _sum -= x[left]
            left += 1

    return length if length != N + 1 else 0


N, S = map(int, input().split())
num_list = list(map(int, input().split()))
print(solve(num_list, S))
