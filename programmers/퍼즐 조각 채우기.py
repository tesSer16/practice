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

    def check_bfs(start, blank):
        q = deque([start])
        visited[start[0]][start[1]] = 1
        point_list = [start]
        min_x = max_x = start[0]
        min_y = max_y = start[1]
        while q:
            x, y = q.popleft()
            for idx, d in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]):
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if (blank and not game_board[nx][ny]) or (not blank and table[nx][ny]):
                        min_x, max_x = min(min_x, nx), max(max_x, nx)
                        min_y, max_y = min(min_y, ny), max(max_y, ny)
                        point_list.append((nx, ny))
                        visited[nx][ny] = 1
                        q.append((nx, ny))

        origin = [[0] * (max_y - min_y + 1) for _ in range(max_x - min_x + 1)]
        for r, c in point_list:
            origin[r - min_x][c - min_y] = 1

        if blank:
            rotated = [origin]
            # print(*origin, sep='\n')
            # print()
            for _ in range(3):
                origin = rotate_matrix(origin)
                rotated.append(origin)

            return rotated

        else:
            for idx in range(space_cnt):
                if not filled[idx] and origin in blank_space[idx]:
                    filled[idx] = 1
                    return sum(map(sum, origin))
            else:
                return 0

    visited = [[0] * n for _ in range(n)]
    blank_space = []
    for i in range(n):
        for j in range(n):
            if not game_board[i][j] and not visited[i][j]:
                blank_space.append(check_bfs((i, j), True))

    space_cnt = len(blank_space)
    filled = [0 for _ in range(space_cnt)]
    visited = [[0] * n for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(n):
            if table[i][j] and not visited[i][j]:
                # answer += check_bfs((i, j), False)
                temp = check_bfs((i, j), False)
                print(temp)
                answer += temp

    return answer


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
