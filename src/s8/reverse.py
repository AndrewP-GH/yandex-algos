import sys
import unittest


def reverse_str(str):
    parts = str.split()[::-1]
    return ' '.join(parts)


if __name__ == '__main__':
    _input = sys.stdin.readline()
    _res = reverse_str(_input)
    print(_res)


class Tests(unittest.TestCase):
    def test_first(self):
        input = 'one two three'
        expected = 'three two one'
        self.assertEqual(reverse_str(input), expected)

    def test_second(self):
        input = 'one two'
        expected = 'two one'
        self.assertEqual(reverse_str(input), expected)
