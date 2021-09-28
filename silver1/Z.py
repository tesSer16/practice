N, r, c = map(int, input().split())


def Z(n, row, column):
    global answer, finished

    if finished:
        return
    if n < 0:
        answer += 1
        return
    rc_list = [[row, column], [row, column + 2 ** n],
               [row + 2 ** n, column], [row + 2 ** n, column + 2 ** n]]

    for rc in rc_list:
        Z(n - 1, *rc)
        if rc == [r, c]:
            finished = False
            print(answer)
            return


finished = False
answer = -1
Z(N - 1, 0, 0)
