def solution(s):
    def transform(string):
        cnt = 0
        while "110" not in string:
            stack = []
            for c in string:
                if c == "0" and stack[-2:] == ["1", "1"]:
                    cnt += 1
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(c)

        i = 0
        for j in range(len(string) - 1, -1, -1):
            if string[j] == "0":
                i = j + 1
                break

        return string[:i] + cnt * "110" + string[i:]

    answer = []
    for x in s:
        answer.append(transform(x))

    return answer


print(solution(["1110","100111100","0111111010"]))
