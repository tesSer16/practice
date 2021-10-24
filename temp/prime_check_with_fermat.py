import random


def R2L(g, k, N):
    if g == 0:
        return 0

    A, B = 1, g
    k = format(k, 'b')

    for ki in k[::-1]:
        if ki == '1':
            A = (A * B) % N
        B = (B * B) % N

    return A


def is_prime(n, t):
    for i in range(1, t + 1):
        a = random.randint(2, n - 2)
        r = R2L(a, n - 1, n)
        if r != 1:
            return "composite"

    return "prime"


if __name__ == "__main__":
    print(is_prime(31, 5))
