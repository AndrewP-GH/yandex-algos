def flowers_field(n, m, field):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[n - 1][1] = field[n - 1][0]
    for i in range(n - 1, -1, -1):
        for j in range(1, m + 1):
            dp[i][j] = field[i][j - 1] + max(dp[i][j - 1], dp[i + 1][j])
    return dp[0][m]


if __name__ == '__main__':
    _n, _m = map(int, input().split())
    _field = [None] * _n
    for _i in range(_n):
        _field[_i] = list(map(int, input()))
    print(flowers_field(_n, _m, _field))
