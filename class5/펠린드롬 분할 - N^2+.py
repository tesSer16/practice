s = ' ' + input()
n = len(s) - 1
d, p = [0] * (n + 1), [0] * (n + 1)
for i in range(1, n + 1):
    d[i] = i
    for j in range(1, i + 1):
        if s[j] == s[i] and (i - j <= 1 or p[j + 1]):
            p[j] = 1
            d[i] = min(d[i], d[j - 1] + 1)
        else:
            p[j] = 0
    print(p[1:i + 1])

print(d[n])
