import unittest


def compare(first, second):
    skip_set = set()
    a = ord('a')
    for i in range(a, ord('z') + 1):
        if (i - a + 1) % 2 == 1:
            skip_set.add(chr(i))
    first_len = len(first)
    second_len = len(second)
    f_ptr, s_ptr = 0, 0
    while True:
        while f_ptr < first_len and first[f_ptr] in skip_set:
            f_ptr += 1
        while s_ptr < second_len and second[s_ptr] in skip_set:
            s_ptr += 1
        if f_ptr == first_len and s_ptr == second_len:
            return 0
        if f_ptr == first_len or s_ptr == second_len:
            if f_ptr == first_len:
                return -1
            else:
                return 1
        if first[f_ptr] == second[s_ptr]:
            f_ptr += 1
            s_ptr += 1
            continue
        if first[f_ptr] < second[s_ptr]:
            return -1
        else:
            return 1


if __name__ == '__main__':
    _f = input()
    _s = input()
    print(compare(_f, _s))


class TestCompare(unittest.TestCase):
    def test_first(self):
        result = compare('gggggbbb', 'bbef')
        self.assertEqual(result, -1)

    def test_second(self):
        result = compare('z', 'aaaaaaa')
        self.assertEqual(result, 1)

    def test_third(self):
        result = compare('ccccz', 'aaaaaz')
        self.assertEqual(result, 0)
