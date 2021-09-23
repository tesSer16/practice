N = int(input())
origin = list(map(int, input().split()))
s = int(input())

i = 0
while s > 0 and i < (N - 1):
    M, j = origin[i], i
    for k in range(i + 1, min(N, i + 1 + s)):
        if M < origin[k]:
            M = origin[k]
            j = k
    s -= (j - i)

    for l in range(j, i, -1):
        origin[l] = origin[l - 1]
    origin[i] = M

    i += 1
        

print(' '.join(map(str, origin)))
