def is_prime(num):
    if num == 1:
        return False
    
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    return prime


def is_awesome_prime(num):
    awe_prime = True
    for i in range(1, len(str(num)) + 1):
        print(i, len(str(num)))
        if not is_prime(num % (10 ** i)):
            awe_prime = False
            break
    return awe_prime



print(is_awesome_prime(357686312646216567629137))
