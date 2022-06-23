import sys
import unittest


def packed_prefix(n, lines):
    pass


def build_line(line):
    stack = []
    i = 0
    local = ''
    while i < len(line):
        ch = line[i]
        if 'a' <= ch <= 'z':
            local += ch
        elif len(local) > 0:
            stack.append(local)
            local = ''
        elif ch.isnumeric():
            stack.append(int(ch))
        i += 1
    if len(local) > 0:
        stack.append(local)

    result = ''
    while len(stack) > 0:
        local = stack.pop()
        if isinstance(local, int):
            result = result * local
        else:
            result = local + result
    return result


if __name__ == '__main__':
    _n = int(input())
    _lines = [None] * _n
    for _i in range(_n):
        _lines[_i] = sys.stdin.readline().rstrip()
    packed_prefix(_n, _lines)


class TestPackedPrefix(unittest.TestCase):
    def test_build_line_1(self):
        line = '2[a]2[ab]'
        exp = 'aaabab'
        self.assertEqual(build_line(line), exp)

    def test_build_line_2(self):
        line = '3[a]2[r2[t]]'
        exp = 'aaarttrtt'
        self.assertEqual(build_line(line), exp)

    def test_build_line_3(self):
        line = 'a2[aa3[b]]'
        exp = 'aaabbbaabbb'
        self.assertEqual(build_line(line), exp)

    def test_build_line_4(self):
        line = '2[abac]a'
        exp = 'abacabaca'
        self.assertEqual(build_line(line), exp)

    def test_build_line_5(self):
        line = '3[aba]'
        exp = 'abaabaaba'
        self.assertEqual(build_line(line), exp)

    def test_build_line_6(self):
        line = '3[aba]c'
        exp = 'abaabaabac'
        self.assertEqual(build_line(line), exp)
