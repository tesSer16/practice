import sys
read = sys.stdin.readline

N = int(read())
dp = []
R1, G1, B1 = map(int, read().split())
R2, G2, B2 = map(int, read().split())
dp.append([2000, R1 + G2, R1 + B2, 2000, G1 + R2, G1 + B2, 2000, B1 + R2, B1 + G2])
for _ in range(N - 2):
    R, G, B = map(int, read().split())
    RR, RG, RB, GG, GR, GB, BB, BR, BG = dp[-1]
    dp.append([min(RG, RB) + R, min(RR, RB) + G, min(RR, RG) + B,
               min(GR, GB) + G, min(GG, GB) + R, min(GG, GR) + B,
               min(BR, BG) + B, min(BB, BG) + R, min(BB, BR) + G])

print(min(dp[-1][i] if i % 3 else 1000 * N for i in range(9)))
