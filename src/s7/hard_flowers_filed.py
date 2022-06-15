def flowers_field(n, m, field):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[n - 1][1] = field[n - 1][0]
    for i in range(n - 1, -1, -1):
        for j in range(1, m + 1):
            dp[i][j] = field[i][j - 1] + max(dp[i][j - 1], dp[i + 1][j])
    path = find_path(n, m, dp)
    return dp[0][m], "".join(reversed(path))


def find_path(n, m, dp):
    path = []
    max_right = m
    for i in range(n):
        j = max_right
        while j > 0:
            if i == n - 1 and j == 1:
                return path
            if dp[i][j - 1] >= dp[i + 1][j] and j > 1:
                path.append('R')
            else:
                path.append('U')
                max_right = j
                break
            j -= 1
    return path


if __name__ == '__main__':
    _n, _m = map(int, input().split())
    _field = [None] * _n
    for _i in range(_n):
        _field[_i] = list(map(int, input()))
    _score, path = flowers_field(_n, _m, _field)
    print(_score)
    print(path)
