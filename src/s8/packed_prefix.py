import sys
import unittest


def packed_prefix(n, lines):
    result = ""
    for i in range(len(lines[0])):
        ch = lines[0][i]
        for j in range(1, n):
            line = lines[j]
            if i > len(line) or line[i] != ch:
                return result
        result += ch
    return result


def unpack(line):
    stack = []
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == '[':
            pass
        elif ch == ']':
            top = stack.pop()
            local = ""
            while not top.isnumeric():
                local = top + local
                top = stack.pop()
            local = int(top) * local
            stack.append(local)
        else:
            stack.append(ch)
        i += 1

    result = ""
    while len(stack) > 0:
        result = stack.pop() + result
    return result


if __name__ == '__main__':
    _n = int(input())
    _lines = [None] * _n
    for _i in range(_n):
        _line = sys.stdin.readline().rstrip()
        _lines[_i] = unpack(_line)
    print(packed_prefix(_n, _lines))


class TestPackedPrefix(unittest.TestCase):
    def test_unpack_line_1(self):
        line = '2[a]2[ab]'
        exp = 'aaabab'
        self.assertEqual(unpack(line), exp)

    def test_unpack_line_2(self):
        line = '3[a]2[r2[t]]'
        exp = 'aaarttrtt'
        self.assertEqual(unpack(line), exp)

    def test_unpack_line_3(self):
        line = 'a2[aa3[b]]'
        exp = 'aaabbbaabbb'
        self.assertEqual(unpack(line), exp)

    def test_unpack_line_4(self):
        line = '2[abac]a'
        exp = 'abacabaca'
        self.assertEqual(unpack(line), exp)

    def test_unpack_line_5(self):
        line = '3[aba]'
        exp = 'abaabaaba'
        self.assertEqual(unpack(line), exp)

    def test_unpack_line_6(self):
        line = '3[aba]c'
        exp = 'abaabaabac'
        self.assertEqual(unpack(line), exp)

    def test_max_prefix_1(self):
        n = 3
        lines = ['aaabab', 'aaarttrtt', 'aaabbbaabbb']
        exp = 'aaa'
        self.assertEqual(packed_prefix(n, lines), exp)

    def test_max_prefix_2(self):
        n = 3
        lines = ['abacabaca', 'abacabaca', 'abaabaaba']
        exp = 'aba'
        self.assertEqual(packed_prefix(n, lines), exp)
