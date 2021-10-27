def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


N = 461
result = []
for n in range(2, N + 1):
    if is_prime(n):
        result.append(n)

print(result)
print(len(result))
