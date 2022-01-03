for a in range(1, 50):
    for b in range(1, 50):
        for c in range(1, 50):
            for d in range(1, 50):
                if a ** 2 + b ** 2 + c ** 2 + d ** 2 == 2022:
                    print(a, b, c, d)
