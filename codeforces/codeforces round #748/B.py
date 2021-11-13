import sys

for _ in range(int(input())):
    n = sys.stdin.readline().strip()
    answer = float('inf')
    for s in ['00', '25', '50', '75']:
        sub_answer = 0
        ptr = len(n) - 1
        while ptr >= 0 and n[ptr] != s[1]:
            sub_answer += 1
            ptr -= 1

        if ptr >= 0:
            ptr -= 1

        while ptr >= 0 and n[ptr] != s[0]:
            sub_answer += 1
            ptr -= 1

        if ptr >= 0 and answer > sub_answer:
            answer = sub_answer

    print(answer)
