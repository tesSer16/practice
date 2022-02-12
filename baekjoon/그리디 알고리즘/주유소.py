N = int(input())

kms = list(map(int, input().split()))
prices = list(map(int, input().split()))

must_go = [prices[0], 0]
answer = 0
dist = kms[0]
for i in range(1, N - 2):
    if must_go[0] > prices[i]:
        answer += must_go[0] * dist
        must_go = [prices[i], i]
        dist = 0
    dist += kms[i]

print(answer + must_go[0] * (dist + kms[N - 2]))
