N, K = map(int, input().split())

answer = 0
while bin(N).count('1') > K:
    temp = 2 ** (bin(N)[::-1].index('1'))
    answer += temp
    N += temp

print(answer)
