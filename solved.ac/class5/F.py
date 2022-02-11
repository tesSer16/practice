import sys
read = sys.stdin.readline


def LCS_length():
    result = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if string1[i] == string2[j]:
                LCS[i][j] = LCS[i - 1][j - 1] + 1
                result = max(result, LCS[i][j])
            else:
                LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

    return result


def LCS_track():
    result = []
    i, j = N, M
    value = LCS[i][j]
    while LCS[i][j]:
        if value == LCS[i - 1][j]:
            i -= 1
        elif value == LCS[i][j - 1]:
            j -= 1
        else:
            result.append(string1[i])
            i, j = i - 1, j - 1
            value = LCS[i][j]

    return result[::-1]


for _ in range(int(read())):
    string1 = [''] + list(read().strip())
    string2 = [''] + list(read().strip())
    N, M = len(string1) - 1, len(string2) - 1
    LCS = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    print(LCS_length())
    print(''.join(LCS_track()))
