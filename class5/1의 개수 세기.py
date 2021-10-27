mem = {0: 0}
_sum = 0
A, B = map(int, input().split())
k1 = 0
while 2 ** k1 - 1 < A:
    _sum += 2 ** k1 + _sum
    k1 += 1
    mem[2 ** k1 - 1] = _sum

k2 = k1
while 2 ** k2 - 1 < B:
    _sum += 2 ** k2 + _sum
    k2 += 1
    mem[2 ** k2 - 1] = _sum


def find(n):
    if n in mem:
        return mem[n]

    k = 0
    while 2 ** k <= n:
        k += 1

    m1 = 2 ** (k - 1)
    m2 = n - m1
    mem[n] = (m2 + 1) + find(m2) + mem[m1 - 1]
    return mem[n]


print(find(B) - find(A - 1))
