class Shark:
    def __init__(self, row, col, spd, dir, size):
        self.row = row
        self.col = col
        self.spd = spd % (2 * (row - 1, col - 1)[(dir - 1) // 2])
        self.dir = dir
        self.size = size

    def move(self, v):
        if self.dir == 1:
            if v < self.row:
                self.row -= v
            else:
                self.row = 0
                self.dir = 2
                self.move(v - self.row)

        if self.dir == 2:
            if v < (R - 1 - self.row):
                self.row += v
            else:
                self.row = R - 1
                self.dir = 1
                self.move(v - (R - 1 - self.row))

        if self.dir == 3:
            if v < self.col:
                self.col -= v
            else:
                self.col = 0
                self.dir = 4
                self.move(v - self.col)

        if self.dir == 4:
            if v < (C - 1 - self.col):
                self.col += v
            else:
                self.col = C - 1
                self.dir = 3
                self.move(v - (C - 1 - self.col))


R, C, M = map(int, input().split())
sharks = []
for _ in range(M):
    sharks.append(Shark(*map(int, input().split())))

for j in range(C):
    # catch sharks

    # move each sharks
    for shark in sharks:
        shark.move(shark.spd)
    # remove intersect
    pass
