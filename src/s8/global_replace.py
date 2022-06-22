import sys
import unittest


def global_replace(text, pattern, replacement):
    positions = search(pattern, text)
    prev_pos = 0
    for pos in positions:
        print(text[prev_pos:pos], end="")
        print(replacement, end="")
        prev_pos = pos + len(pattern)
    print(text[prev_pos:])


def search(p, text):
    result = []
    s = p + '#' + text
    len_p = len(p)
    pi = [0] * len_p
    pi_prev = 0
    for i in range(1, len(s)):
        k = pi_prev
        while k > 0 and s[k] != s[i]:
            k = pi[k - 1]
        if s[k] == s[i]:
            k += 1
        if i < len_p:
            pi[i] = k
        pi_prev = k
        if k == len_p:
            result.append(i - 2 * len_p)
    return result


if __name__ == '__main__':
    _text = sys.stdin.readline().rstrip()
    _s = sys.stdin.readline().rstrip()
    _t = sys.stdin.readline().rstrip()
    global_replace(_text, _s, _t)
    # _res = global_replace(_text, _s, _t)
    # print(_res)


# class TestGlobalReplace(unittest.TestCase):
#     def test_1(self):
#         text = 'pingpong'
#         s = 'ng'
#         r = 'mpi'
#         exp = 'pimpipompi'
#         self.assertEqual(global_replace(text, s, r), exp)
#
#     def test_2(self):
#         text = 'aaa'
#         s = 'a'
#         r = 'ab'
#         exp = 'ababab'
#         self.assertEqual(global_replace(text, s, r), exp)
