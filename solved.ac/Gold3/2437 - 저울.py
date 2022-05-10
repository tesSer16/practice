N = int(input())
cover = 0
arr = sorted(map(int, input().split()))
for a in arr:
    if cover + 1 >= a:
        cover += a
    else:
        break

print(cover + 1)
