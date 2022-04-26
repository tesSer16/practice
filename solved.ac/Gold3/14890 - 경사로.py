def check(arr):
    counter = 1
    is_down = False
    current = arr[0]
    for x in range(1, len(arr)):
        if not is_down:
            if arr[x] > current:
                if counter < L or current + 1 < arr[x]:
                    return False
                current = arr[x]
                counter = 0
            elif arr[x] < current:
                if arr[x] < current - 1:
                    return False
                is_down = True
                counter = 0
                current = arr[x]
        else:
            if arr[x] > current:
                if counter < 2 * L or current + 1 < arr[x]:
                    return False
                else:
                    current = arr[x]
                    counter = 0
                    is_down = False
            elif arr[x] < current:
                if counter < L or arr[x] < current - 1:
                    return False
                else:
                    current = arr[x]
                    counter = 0
        counter += 1

    if (not is_down) or (counter >= L):
        return True

    return False


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
_sum = 0
for i in range(N):
    val = check(board[i])
    _sum += val

for j in range(N):
    val = check([board[i][j] for i in range(N)])
    _sum += val

print(_sum)
