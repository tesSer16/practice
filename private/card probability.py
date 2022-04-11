from itertools import combinations


def check(hand):
    for comb in re_combs:
        for c in comb:
            if c not in hand:
                break
        else:
            return True

    return False


def ban_check(hand):
    for b in range(len(banned)):
        if -(b + 1) in hand:
            return False

    return True


cards = 40  # int(input("Total cards: "))
hands = 5  # int(input("Start hands: "))
requirements = [1, 1, 1, 1, 1]
re_combs = [(1, 2, 3, 4, 5)]

banned = [1, 1, 1]
pool = []
for i, v in enumerate(requirements):
    for _ in range(v):
        pool.append(i + 1)

for i, v in enumerate(banned):
    for _ in range(v):
        pool.append(-(i + 1))

for _ in range(cards - len(pool)):
    pool.append(0)

total = 0
ans = 0
for case in combinations(pool, hands):
    total += 1
    if check(case) and ban_check(case):
        ans += 1

print(total)
print(f"{ans / total * 100:.3F}%")
