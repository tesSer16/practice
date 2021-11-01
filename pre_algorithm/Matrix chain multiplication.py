import sys


def main():
    n = int(sys.stdin.readline())
    r_and_c = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]

    sizes = [r for r, _ in r_and_c]
    sizes.append(r_and_c[-1][1])
    dp = [[0] * n for _ in range(n)]
    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            sz_ij = sizes[i] * sizes[j + 1]
            m = min(min_ik + min_kj + sz_ij * sz_k for min_ik, min_kj, sz_k in
                    zip(dp[i][i:j], dp[j][i + 1:j + 1], sizes[i + 1:j + 1]))
            dp[i][j] = dp[j][i] = m

    print(dp[0][n - 1])


if __name__ == '__main__':
    main()