import sys


def check(x, y):
    if 0 <= x < N and 0 <= y < N and depart[x][y] == "1":
        depart[x][y] = 1
        answer[-1] += 1

        check(x - 1, y)
        check(x + 1, y)
        check(x, y - 1)
        check(x, y + 1)
    else:
        return


N = int(input())
depart = [list(sys.stdin.readline().strip()) for _ in range(N)]

answer = []
for i in range(N):
    for j in range(N):
        if depart[i][j] == "1":
            answer.append(0)
            check(i, j)

answer.sort()
print(len(answer))
print(*answer, sep='\n')
