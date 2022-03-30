def rotate_matrix(mat, size):
    n = size - 1
    for d in range(size // 2):
        for x in range(d, n - d):
            mat[x][d], mat[n - d][x], mat[n - x][n - d], mat[d][n - x] = \
                mat[d][n - x], mat[x][d], mat[n - d][x], mat[n - x][n - d]
