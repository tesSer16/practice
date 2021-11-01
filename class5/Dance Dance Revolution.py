num_list, dum = input().split()
N = len(num_list)
dp = [[0] * 10 for _ in range(N)]  # 12 13 14 23 24 34 10 20 30 40
order = {1: (0, 2, 1, 2, 0, 1, 0, 1, 2),
         2: (0, 3, 3, 0, 4, 5, 0, 4, 5),
         3: (3, 5, 1, 2, 5, 3, 1, 3, 5),
         4: (2, 5, 4, 5, 2, 4, 2, 4, 5)}

factor = [4, 4, 3, 3, 3, 3, 1, 1, 1]
dp[0][num_list[0] + 5] = 2

for i in range(1, N):

