import sys


def common_subarray():
    n = int(input())
    first = sys.stdin.readline().rstrip().split()
    m = int(input())
    second = sys.stdin.readline().rstrip().split()
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if first[i] == second[j]:
                matrix[j][i] = 1 + (matrix[j + 1][i + 1] if i + 1 < n and j + 1 < m else 0)
    max_len = 0
    for row in matrix:
        for col in row:
            max_len = max(max_len, col)
    return max_len


if __name__ == '__main__':
    res = common_subarray()
    print(res)
