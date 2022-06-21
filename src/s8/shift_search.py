import sys
import unittest


def shift_search(n, x, m, a) -> [int]:
    diff = [a_1 - a_2 for a_1, a_2 in zip(a[:-1], a[1:])]
    m -= 1
    result = []
    for i in range(n - m):
        success = True
        for j in range(m):
            n = x[i + j + 1]
            c = x[i + j]
            if c - n != diff[j]:
                success = False
                break
        if success:
            result.append(i + 1)
    return result


if __name__ == '__main__':
    _n = int(sys.stdin.readline())
    _x = [*map(int, sys.stdin.readline().split())]
    _m = int(sys.stdin.readline())
    _a = [*map(int, sys.stdin.readline().split())]
    _res = shift_search(_n, _x, _m, _a)
    print(' '.join(map(str, _res)))


class TestShiftSearch(unittest.TestCase):
    def test_first(self):
        result = shift_search(9, [3, 9, 1, 2, 5, 10, 9, 1, 7], 2, [4, 10])
        self.assertEqual(result, [1, 8])

    def test_second(self):
        result = shift_search(5, [1, 2, 3, 4, 5], 3, [10, 11, 12])
        self.assertEqual(result, [1, 2, 3])
