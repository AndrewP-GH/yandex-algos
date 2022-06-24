import sys
import unittest

end_word_marker = '$'


def is_pony(string: str, words: [str]) -> bool:
    tree = build_prefix_tree(words)
    return check_string(string, tree)


def check_string(string: str, tree: dict) -> bool:
    node = tree
    i = 0
    len_s = len(string)
    possible_ways = []
    while i < len_s:
        letter = string[i]
        if letter not in node:
            break
        if end_word_marker in node[letter]:
            possible_ways.append(i)
        node = node[letter]
        i += 1
    if i == len_s and end_word_marker in node:
        return True
    while len(possible_ways) > 0:
        i = possible_ways.pop()
        if check_string(string[i + 1:], tree):
            return True
    return False


def build_prefix_tree(words: [str]) -> dict:
    tree = {}
    for word in words:
        node = tree
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[end_word_marker] = True
    return tree


if __name__ == '__main__':
    _t = sys.stdin.readline().rstrip()
    _n = int(input())
    _words = [None] * _n
    for _i in range(_n):
        _words[_i] = sys.stdin.readline().rstrip()
    _result = is_pony(_t, _words)
    print('YES' if _result else 'NO')


class IsPonyTest(unittest.TestCase):
    def test_1(self):
        t = 'examiwillpasstheexam'
        words = ['will', 'pass', 'the', 'exam', 'i']
        exp = True
        self.assertEqual(is_pony(t, words), exp)

    def test_2(self):
        t = 'abacaba'
        words = ['abac', 'caba']
        exp = False
        self.assertEqual(is_pony(t, words), exp)

    def test_3(self):
        t = 'abacaba'
        words = ['abac', 'caba', 'aba']
        exp = True
        self.assertEqual(is_pony(t, words), exp)
