from copy import deepcopy


class Shark:
    def __init__(self, row, col, spd, dir):
        self.row = row
        self.col = col
        self.spd = spd % (2 * (R - 1, C - 1)[(dir - 1) // 2])
        self.dir = dir

    def move(self, v):
        if self.dir == 1:
            if v < self.row:
                self.row -= v
            else:
                temp, self.row = self.row, 0
                self.dir = 2
                self.move(v - temp)

        elif self.dir == 2:
            if v < (R - 1 - self.row):
                self.row += v
            else:
                temp, self.row = self.row, R - 1
                self.dir = 1
                self.move(v - (R - 1 - temp))

        elif self.dir == 4:
            if v < self.col:
                self.col -= v
            else:
                temp, self.col = self.col, 0
                self.dir = 3
                self.move(v - temp)

        elif self.dir == 3:
            if v < (C - 1 - self.col):
                self.col += v
            else:
                temp, self.col = self.col, C - 1
                self.dir = 4
                self.move(v - (C - 1 - temp))


R, C, M = map(int, input().split())
sharks = {}
board = [[0] * C for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[z] = Shark(r - 1, c - 1, s, d)
    board[r - 1][c - 1] = z

total_size = 0
for j in range(C):
    # catch sharks
    for i in range(R):
        if board[i][j]:
            total_size += board[i][j]
            del sharks[board[i][j]]
            board[i][j] = 0
            break

    # move each sharks
    new_board = [[0] * C for _ in range(R)]
    terminate = []
    for size, shark in sharks.items():
        shark.move(shark.spd)
        if new_board[shark.row][shark.col]:
            if new_board[shark.row][shark.col] > size:
                terminate.append(size)
            else:
                terminate.append(new_board[shark.row][shark.col])
                new_board[shark.row][shark.col] = size
        else:
            new_board[shark.row][shark.col] = size

    for t in terminate:
        del sharks[t]
    board = deepcopy(new_board)
print(total_size)
