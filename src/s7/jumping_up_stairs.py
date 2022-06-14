def jumping_up_stairs(n, k):
    m = (10 ** 9) + 7
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, k + 1):
            if i - j >= 0:
                dp[i] = (dp[i] + dp[i - j]) % m
    return dp[n]


if __name__ == '__main__':
    _n, _k = map(int, input().split())
    print(jumping_up_stairs(_n, _k))
