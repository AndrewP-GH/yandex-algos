import collections
import sys
import unittest


class State:
    def __init__(self):
        self._queue = collections.deque()
        self._possible_ways = set()

    def add(self, way: int):
        if way not in self._possible_ways:
            self._possible_ways.add(way)
            self._queue.append(way)

    def move_next(self) -> bool:
        return len(self._possible_ways) > 0

    def current(self) -> int:
        way = self._queue.popleft()
        self._possible_ways.remove(way)
        return way


def is_pony(string: str, words: [str]) -> bool:
    end_word_marker = '$'
    tree = build_prefix_tree(words, end_word_marker)
    state = State()
    state.add(0)
    while state.move_next():
        start = state.current()
        if check_string(string, tree, end_word_marker, start, state):
            return True
    return False


def check_string(string: str, tree: dict, end_word_marker: str, start: int, state: State) -> bool:
    node = tree
    i = start
    len_s = len(string)
    while i < len_s:
        letter = string[i]
        node = node.get(letter)
        if node is None:
            return False
        next_index = i + 1
        if end_word_marker in node \
                and next_index < len_s \
                and string[next_index] in tree:
            possible_way = next_index
            state.add(possible_way)
        i = next_index
    return end_word_marker in node


def build_prefix_tree(words: [str], end_word_marker: str) -> dict:
    tree = {}
    for word in words:
        node = tree
        for letter in word:
            if letter == '\n':
                continue
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
        _words[_i] = sys.stdin.readline()
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
