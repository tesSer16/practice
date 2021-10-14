def solution(game_board, table):
    from collections import deque
    n = len(game_board)

    def rotate_matrix(matrix):
        M, N = len(matrix), len(matrix[0])
        result = [[0] * M for _ in range(N)]

        for r in range(M):
            for c in range(N):
                result[N - c - 1][r] = matrix[r][c]

        return result

    def check_bfs(start):
        q = deque([start])
        visited[start[0]][start[1]] = 1
        point_list = [start]
        min_x = max_x = start[0]
        min_y = max_y = start[1]
        while q:
            x, y = q.popleft()
            for idx, d in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]):
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and not game_board[nx][ny]:
                    min_x, max_x = min(min_x, nx), max(max_x, nx)
                    min_y, max_y = min(min_y, ny), max(max_y, ny)
                    point_list.append((nx, ny))
                    visited[nx][ny] = 1
                    q.append((nx, ny))

        origin = [[0] * (max_y - min_y + 1) for _ in range(max_x - min_x + 1)]
        for r, c in point_list:
            origin[r - min_x][c - min_y] = 1

        print(*origin, sep='\n')
        print()

    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not game_board[i][j] and not visited[i][j]:
                check_bfs((i, j))


board = [[1, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 0],
         [0, 1, 1, 0, 0, 1],
         [1, 1, 0, 1, 1, 1],
         [1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 0]]

tab = [[1, 0, 0, 1, 1, 0],
       [1, 0, 1, 0, 1, 0],
       [0, 1, 1, 0, 1, 1],
       [0, 0, 1, 0, 0, 0],
       [1, 1, 0, 1, 1, 0],
       [0, 1, 0, 0, 0, 0]]

solution(board, tab)
