import unittest


def count_prefix_function(s: str) -> [int]:
    pi = [0] * len(s)
    for i in range(1, len(s)):
        k = pi[i - 1]
        while k > 0 and s[i] != s[k]:
            k = pi[k - 1]
        if s[i] == s[k]:
            k += 1
        pi[i] = k
    return pi


def prefix_function_view(s):
    res = count_prefix_function(s)
    return ' '.join(map(str, res))


if __name__ == '__main__':
    _s = input()
    _res = prefix_function_view(_s)
    print(_res)


class TestPrefixFunction(unittest.TestCase):
    def test_prefix_function(self):
        s = 'abracadabra'
        exp = '0 0 0 1 0 1 0 1 2 3 4'
        self.assertEqual(prefix_function_view(s), exp)

    def test_prefix_function_2(self):
        s = 'xxzzxxz'
        exp = '0 1 0 0 1 2 3'
        self.assertEqual(prefix_function_view(s), exp)

    def test_prefix_function_3(self):
        s = 'aaaaa'
        exp = '0 1 2 3 4'
        self.assertEqual(prefix_function_view(s), exp)
