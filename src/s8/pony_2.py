import sys
import unittest

end_word_marker = '$'


def is_pony(string: str, bor: {}) -> bool:
    l_s = len(string)
    dp = [False] * (l_s + 1)
    dp[0] = True
    for i in range(l_s):
        j = i
        while j >= 0:
            letter = string[j]
            node = bor.get(letter) if i == j else node.get(letter)
            if node is None:
                break
            if end_word_marker in node and dp[j]:
                dp[i + 1] = True
                break
            j -= 1
    return dp[l_s]


def add_word(bor: {}, word: str):
    node = bor
    for letter in reversed(word):
        if letter == '\n':
            continue
        if letter not in node:
            node[letter] = {}
        node = node[letter]
    node[end_word_marker] = True


if __name__ == '__main__':
    _t = sys.stdin.readline().rstrip()
    _n = int(input())
    _bor = {}
    for _ in range(_n):
        add_word(_bor, sys.stdin.readline())
    _result = is_pony(_t, _bor)
    print('YES' if _result else 'NO')


class IsPonyTest(unittest.TestCase):
    def test_1(self):
        t = 'examiwillpasstheexam'
        words = ['will', 'pass', 'the', 'exam', 'i']
        bor = {}
        for word in words:
            add_word(bor, word)
        exp = True
        self.assertEqual(is_pony(t, bor), exp)

    def test_2(self):
        t = 'abacaba'
        words = ['abac', 'caba']
        bor = {}
        for word in words:
            add_word(bor, word)
        exp = False
        self.assertEqual(is_pony(t, bor), exp)

    def test_3(self):
        t = 'abacaba'
        words = ['abac', 'caba', 'aba']
        bor = {}
        for word in words:
            add_word(bor, word)
        exp = True
        self.assertEqual(is_pony(t, bor), exp)

    def test_4(self):
        t = 'sscevscescescscsscevscevscesscsc'
        words = ['sce', 's', 'scev', 'sc']
        bor = {}
        for word in words:
            add_word(bor, word)
        exp = True
        self.assertEqual(is_pony(t, bor), exp)

    def test_5(self):
        t = 'axymaxymaxyaxymaxyaxymaxymaxax'
        words = ['axy', 'axym', 'ax', 'a']
        bor = {}
        for word in words:
            add_word(bor, word)
        exp = True
        self.assertEqual(is_pony(t, bor), exp)

    def test_6(self):
        t = 'hfbfhfbfhfbfhhfbfhfbhfbhhhhfhfbf'
        words = ['hfb', 'hf', 'hfbf', 'h']
        bor = {}
        for word in words:
            add_word(bor, word)
        exp = True
        self.assertEqual(is_pony(t, bor), exp)

    def test_7(self):
        t = 'bwvfbtrjqpbwvfbbwvbwbbwbbwvbwvf'
        words = ['bwvf', 'b', 'bw', 'bwv']
        bor = {}
        for word in words:
            add_word(bor, word)
        exp = False
        self.assertEqual(is_pony(t, bor), exp)
