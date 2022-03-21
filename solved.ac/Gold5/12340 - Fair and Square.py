import sys
read = sys.stdin.readline


def is_palindrome(num):
    return str(num) == str(num)[::-1]


ans = []
for n in range(1, 10**7 + 1):
    if is_palindrome(n) and is_palindrome(n ** 2):
        ans.append(n ** 2)

for i in range(int(read())):
    A, B = map(int, read().split())
    j = 0
    while ans[j] < A:
        j += 1
    left = j

    while j < len(ans) and ans[j] <= B:
        j += 1
    print(f"Case #{i + 1}: {j - left}")
