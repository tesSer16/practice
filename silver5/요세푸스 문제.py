N, K = map(int, input().split())

work_list = [i + 1 for i in range(N)]
print("<", end="")
idx = K - 1
for n in range(N, 1, -1):
    print(work_list.pop(idx), end=", ")
    idx = (idx + K - 1) % (n - 1)

print("%d>" % work_list[0])
