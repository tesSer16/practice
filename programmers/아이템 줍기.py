def solution(rectangle, characterX, characterY, itemX, itemY):
    import sys
    sys.setrecursionlimit(10 ** 6)

    def void(r, c, value):
        visited[r][c] = value
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < max_x and 0 <= nc < max_y and not board[nr][nc] and not visited[nr][nc]:
                void(nr, nc, value)

    def is_edge(r, c):
        for dr, dc in adj:
            nr, nc = r + dr, c + dc
            if visited[nr][nc] == -1:
                return True

    max_x = max_y = 0
    for rect in rectangle:
        x1, y1, x2, y2 = rect
        max_x = max(x2, max_x)
        max_y = max(y2, max_y)

    max_x = 2 * (max_x + 1)
    max_y = 2 * (max_y + 1)
    board = [[0] * max_y for _ in range(max_x)]
    for rect in rectangle:
        x1, y1, x2, y2 = rect
        for i in range(2 * x1, 2 * x2 + 1):
            for j in range(2 * y1, 2 * y2 + 1):
                board[i][j] = 1

    visited = [[0] * max_y for _ in range(max_x)]
    void(0, 0, -1)

    print(*board, sep='\n')
    adj = [(-1, -1), (-1, 0), (-1, 1),
           (0, -1), (0, 1),
           (1, -1), (1, 0), (1, 1)]

    edges = []
    for x in range(max_x):
        for y in range(max_y):
            if board[x][y] and is_edge(x, y):
                edges.append((x, y))
                break
        else:
            continue
        break

    start = edges.pop()
    current = start
    while True:
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if board[nx][ny] and is_edge(nx, ny) and (nx, ny) not in edges:
                current = (nx, ny)
                edges.append(current)
                break

        if current == start:
            break
    for x, y in edges:
        board[x][y] = 2

    char = edges.index((2 * characterX, 2 * characterY)) // 2
    item = edges.index((2 * itemX, 2 * itemY)) // 2
    e_cnt = len(edges) // 2
    print(char, item, e_cnt)

    a, b = min(char, item), max(char, item)
    answer = min(b - a, a + e_cnt - 1 - b)
    return answer


print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
