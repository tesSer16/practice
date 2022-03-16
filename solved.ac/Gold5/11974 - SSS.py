import sys
read = sys.stdin.readline

N = int(read())
left = [0] * 7
left[0] = -1
right = [0] * 7
_sum = 0
for i in range(N):
    _sum = (_sum + int(read())) % 7
    if not left[_sum]:
        left[_sum] = i + 1
    else:
        right[_sum] = i + 1

print(left)
print(right)
print(max([right[0] - left[0] - 1] + [right[i] - left[i] for i in range(1, 7)]) if any(right) else 0)
