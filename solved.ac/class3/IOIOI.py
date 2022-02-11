N = int(input())
M = int(input())
string = input()

cnt, counter, idx = 0, 0, 1
while idx < M - 1:
    if string[idx - 1: idx + 2] == 'IOI':
        counter += 1
        if counter == N:
            counter -= 1
            cnt += 1
        idx += 1
    else:
        counter = 0
    idx += 1

print(cnt)
