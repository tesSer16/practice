import sys
read = sys.stdin.readline

for _ in range(int(read())):
    a, b, c, x, y = map(int, read().split())
    ra, rb = x - a, y - b
    if ra <= 0 and rb <= 0:
        print("YES")
    elif ra > 0 and rb > 0:
        print("YES" if ra + rb <= c else "NO")
    else:
        rc = ra if ra > 0 else rb
        print("YES" if rc <= c else "NO")
