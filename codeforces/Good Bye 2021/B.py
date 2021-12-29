for _ in range(int(input())):
    n = int(input())
    s = input()
    i = 1
    while i < n and s[i] <= s[i - 1]:
        if s[i] == s[i - 1] and i < 2:
            break
        i += 1

    print(s[:i] + s[:i][::-1])
