N = int(input())
M = int(input())

button = [str(i) for i in range(10)]
if M > 0:
    broken = list(map(str, input().split()))
    button = list(filter(lambda x: x not in broken, button))

current_ch = 100
m = abs(current_ch - N)

for ch in range(1000000):
    for j in range(len(str(ch))):
        if str(ch)[j] not in button:
            break

        elif len(str(ch)) - 1 == j:
            m = min(m, abs(ch - N) + len(str(ch)))

print(m)
