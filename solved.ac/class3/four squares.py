class Solve:
    def __init__(self):
        self.result = 4
        n = int(input())
        self.solve(n, 1)

    def solve(self, num, cnt):
        for a in range(int(num**0.5), int((num//(4 - cnt + 1))**0.5), -1):
            if num == a*a:
                self.result = min(cnt, self.result)
            else:
                self.solve(num - a*a, cnt + 1)


answer = Solve()
print(answer.result)
