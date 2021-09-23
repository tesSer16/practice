N = int(input())
price = list(map(int, input().split()))
M = int(input())

product = [0] * 10
max_length = 0
max_lengths = [0] * 10
for i in range(1, 11):
    value = M // price[i]
    if value > max_length:
    
