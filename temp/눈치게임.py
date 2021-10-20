def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


N = 460
result = []
for i in range(2, N + 1):
    if is_prime(i):
        result.append(i)

print(result)
print(len(result))
