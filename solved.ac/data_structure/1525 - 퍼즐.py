from collections import deque


def change(cur, x, y, ix, iy):
    arr = [list(f"{cur // 10 ** 6:03d}"),
           list(f"{cur % 10 ** 6 // 1000:03d}"),
           list(f"{cur % 1000:03d}")]

    arr[x][y], arr[ix][iy] = arr[ix][iy], arr[x][y]
    # print(*arr, sep='\n')
    return int(''.join(arr[0])) * 10 ** 6 + int(''.join(arr[1])) * 1000 + int(''.join(arr[2]))


init = 0
izx = izy = -1
for i in range(2, -1, -1):
    temp = ''.join(input().split())
    if temp.find('0') > 0:
        izx, izy = 2 - i, temp.find('0')
    init += int(temp) * 10 ** (3 * i)

# print(init)
q = deque([(init, izx, izy, 0)])
check = set()

while q:
    current, zx, zy, num = q.popleft()
    if current == 123456780:
        print(num)
        break
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx, ny = zx + dx, zy + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            tmp = change(current, zx, zy, nx, ny)
            # print(num + 1)
            if tmp not in check:
                q.append((tmp, nx, ny, num + 1))
                check.add(tmp)

else:
    print(-1)
