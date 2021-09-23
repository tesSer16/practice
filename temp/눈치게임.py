def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


N = 439
result = []
for i in range(2, N):
    if is_prime(i):
        result.append(i)
