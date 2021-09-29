input()
num_list = [0] + sorted(list(map(int, input().split())))
n = int(input())
for i in range(len(num_list)):
    if num_list[i] > n:
        break

if n != num_list[i]:
    cnt = n - num_list[i - 1]
    if cnt:
        print(cnt * (num_list[i] - n - 1) + cnt - 1)
    else:
        print(0)

else:
    print(0)
