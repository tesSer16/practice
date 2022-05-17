import os
import time


def cal_num(x, y):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx, ny = x + dx, y + dy
            if 0 <= nx < SIZE and 0 <= ny < SIZE:
                if dx == dy == 0 or board[nx][ny] == -1:
                    continue
                board[nx][ny] += 1


def console_print():
    os.system('cls')
    for i in range(SIZE):
        for j in range(SIZE):
            if not checked[i][j]:
                print('?', end=" ")
            else:
                print(board[i][j] if board[i][j] >= 0 else "※", end=" ")
        print()


def blank_check(x, y):
    checked[x][y] = 1
    for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < SIZE and 0 <= ny < SIZE and not checked[nx][ny]:
            if not board[nx][ny]:
                blank_check(nx, ny)
            else:
                checked[nx][ny] = 1


def explode():
    console_print()
    input("MINE EXPLODED!!!...")


def clear():
    for x, y in mines:
        checked[x][y] = 1
    console_print()
    end = time.time()
    input("CLEAR!!! %.3f" % (end - start))


if __name__ == "__main__":
    SIZE = 9
    mines = (1, 0), (1, 3), (2, 8), (4, 4), (6, 1), (6, 4), (7, 2), (7, 3), (7, 6), (8, 7)
    board = [[0] * SIZE for _ in range(SIZE)]
    for r, c in mines:
        board[r][c] = -1
        cal_num(r, c)

    # print(*board, sep='\n')

    checked = [[0] * SIZE for _ in range(SIZE)]
    cnt, goal = 0, SIZE * SIZE - len(mines)
    start = time.time()
    while True:
        console_print()
        r, c = -1, -1
        try:
            r, c = map(int, input("Please input -> row col: ").split())
            if checked[r][c]:
                raise ValueError
        except ValueError:
            print("Invalid Input!")
            continue

        if board[r][c] == 0:
            blank_check(r, c)
            continue
        elif board[r][c] == -1:
            checked[r][c] = 1
            explode()
            break
        elif cnt == goal:
            clear()
            break

        checked[r][c] = 1
        cnt += 1
