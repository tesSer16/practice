import sys

K, N = map(int, input().split())
LAN_cables = [int(sys.stdin.readline()) for _ in ' ' * K]

start, end = 1, max(LAN_cables)
mid = (start + end) // 2
while start + 1 < end:
    mid = (start + end) // 2
    print(start, end, mid)
    cnt = 0
    for lc in LAN_cables:
        cnt += lc // mid

    if cnt >= N:
        start = mid
    else:
        end = mid

print(start)
