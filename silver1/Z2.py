from functools import reduce


def matrixBS(start, end):
    global answer

    def stair(x):
        if x <= 0:
            return 0
        else:
            return 1

    def dot(x, y):
        if len(x) == len(y):
            return sum([xi * yi for xi, yi in zip(x, y)])
        else:
            return False

    middle = [(s + e) // 2 for s, e in zip(start, end)]
    num = reduce(lambda x, y: x * y, [e - m for m, e in zip(middle, end)])
    # print(start, end)

    if middle == target:
        if start != end:
            answer += num - 1
        return
    else:
        state = list(map(stair, [t - m for t, m in zip(target, middle)]))
        answer += num * dot(state, z)
        matrixBS([start[i] + (end[i] - middle[i]) * state[i] for i in range(len(target))],
                 [middle[i] + (end[i] - middle[i]) * state[i] for i in range(len(target))])


answer = 0
N, r, c = map(int, input().split())

target = [r, c]
z = (2, 1)
matrixBS((0, 0), (2 ** N - 1, 2 ** N - 1))
print(answer)
