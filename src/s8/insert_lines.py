import unittest


def insert_lines(s: str, n: int, lines: [str]) -> str:
    lines = sorted(lines, key=lambda x: x[1])
    s_ptr = 0
    result = []
    for line, i in lines:
        while s_ptr < i:
            result.append(s[s_ptr])
            s_ptr += 1
        result += line
    while s_ptr < len(s):
        result.append(s[s_ptr])
        s_ptr += 1
    return ''.join(result)


if __name__ == '__main__':
    _s = input()
    _n = int(input())
    _lines = [None] * _n
    for _i in range(_n):
        _line = input().split()
        _str, _num = _line[0], int(_line[1])
        _lines[_i] = (_str, _num)
    print(insert_lines(_s, _n, _lines))


class TestInsertLines(unittest.TestCase):
    def test_first(self):
        result = insert_lines('abacaba', 3, [('queue', 2), ('deque', 0), ('stack', 7)])
        self.assertEqual(result, 'dequeabqueueacabastack')

    def test_second(self):
        result = insert_lines('kukareku', 2, [('p', 1), ('q', 2)])
        self.assertEqual(result, 'kpuqkareku')
