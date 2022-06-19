# Отчет 69046535: https://contest.yandex.ru/contest/25597/run-report/69046535/
#

import sys
import unittest


def levenshtein_distance(first: str, second: str) -> int:
    n = len(first)
    m = len(second)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    return dp[n][m]


if __name__ == '__main__':
    _first = sys.stdin.readline()
    _second = sys.stdin.readline()
    _res = levenshtein_distance(_first, _second)
    print(_res)


class Tests(unittest.TestCase):
    def test_first(self):
        first = 'abacaba'
        second = 'abaabc'
        expected = 2
        self.assertEqual(levenshtein_distance(first, second), expected)

    def test_second(self):
        first = 'innokentiy'
        second = 'innnokkentia'
        expected = 3
        self.assertEqual(levenshtein_distance(first, second), expected)

    def test_third(self):
        first = 'r'
        second = 'x'
        expected = 1
        self.assertEqual(levenshtein_distance(first, second), expected)
