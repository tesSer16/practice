N = int(input())
sol = sorted(list(map(int, input().split())))
min_val = [float('inf'), -1, -1, -1]
for left in range(N - 2):
    mid, right = left + 1, N - 1
    while mid < right:
        value = sol[left] + sol[mid] + sol[right]
        if min_val[0] > abs(value):
            min_val = [abs(value), left, mid, right]

        if value > 0:
            right -= 1
        elif value < 0:
            mid += 1
        else:
            print(sol[left], sol[mid], sol[right])
            exit()

print(*(sol[i] for i in min_val[1:]))
