import sys
import unittest

end_word_marker = '$'
possible_ways = set()


def is_pony(string: str, words: [str]) -> bool:
    tree = build_prefix_tree(words)
    return check_string(string, string, tree, 0)


def check_string(string: str, sub_string: str, tree: dict, shift: int) -> bool:
    node = tree
    i = 0
    len_s = len(sub_string)
    while i < len_s:
        letter = sub_string[i]
        if letter not in node:
            break
        next_index = i + 1
        if end_word_marker in node[letter] \
                and next_index < len_s \
                and sub_string[next_index] in tree:
            possible_ways.add(next_index + shift)
        node = node[letter]
        i = next_index
    if i == len_s and end_word_marker in node:
        return True
    while len(possible_ways) > 0:
        pos = next(iter(possible_ways))
        possible_ways.remove(pos)
        if check_string(string, string[pos:], tree, pos):
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

    def test_4(self):
        t = 'sscevscescescscsscevscevscesscsc'
        words = ['sce', 's', 'scev', 'sc']
        exp = True
        self.assertEqual(is_pony(t, words), exp)

    def test_5(self):
        t = 'axymaxymaxyaxymaxyaxymaxymaxax'
        words = ['axy', 'axym', 'ax', 'a']
        exp = True
        self.assertEqual(is_pony(t, words), exp)

    def test_6(self):
        t = 'hfbfhfbfhfbfhhfbfhfbhfbhhhhfhfbf'
        words = ['hfb', 'hf', 'hfbf', 'h']
        exp = True
        self.assertEqual(is_pony(t, words), exp)

    def test_7(self):
        t = 'bwvfbtrjqpbwvfbbwvbwbbwbbwvbwvf'
        words = ['bwvf', 'b', 'bw', 'bwv']
        exp = False
        self.assertEqual(is_pony(t, words), exp)
