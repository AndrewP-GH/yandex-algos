import sys
import unittest

end_word_marker = '$'


def is_pony(string: str, words: [str]) -> bool:
    tree = build_prefix_tree(words)
    possible_ways = set()
    possible_ways.add(0)
    while len(possible_ways) > 0:
        pos = next(iter(possible_ways))
        possible_ways.remove(pos)
        if check_string(string[pos:], tree, pos, possible_ways):
            return True
    return False


def check_string(string: str, tree: dict, shift: int, possible_ways: set) -> bool:
    node = tree
    i = 0
    len_s = len(string)
    while i < len_s:
        letter = string[i]
        if letter not in node:
            break
        next_index = i + 1
        if end_word_marker in node[letter] \
                and next_index < len_s \
                and string[next_index] in tree:
            possible_way = next_index + shift
            possible_ways.add(possible_way)
        node = node[letter]
        i = next_index
    return i == len_s and end_word_marker in node


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
