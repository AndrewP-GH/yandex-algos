import sys
import unittest


def read_data():
    a = int(input())
    m = int(input())
    s = sys.stdin.readline().rstrip()
    return a, m, s


def polynomial_hash(a, m, s):
    result = 0
    for ch in s:
        result = (result * a + ord(ch)) % m
    return result


if __name__ == '__main__':
    input = read_data()
    output = polynomial_hash(*input)
    print(output)


class Tests(unittest.TestCase):
    def test_first(self):
        res = polynomial_hash(123, 100003, 'a')
        self.assertEqual(res, 97)

    def test_second(self):
        res = polynomial_hash(123, 100003, 'hash')
        self.assertEqual(res, 6080)

    def test_third(self):
        res = polynomial_hash(123, 100003, 'HaSH')
        self.assertEqual(res, 56156)
