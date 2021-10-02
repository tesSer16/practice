n = int(input())


def solve():
    for a in range(255):
        for b in range(255):
            for c in range(255):
                for d in range(255):
                    if n == a**2 + b**2 + c**2 + d**2:
                        return a, b, c, d


print(solve())
