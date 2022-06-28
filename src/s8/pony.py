from queue import PriorityQueue
import sys
import unittest

end_word_marker = '$'


class State:
    def __init__(self):
        self._queue = PriorityQueue()
        self._possible_ways = set()

    def add(self, way: int):
        if way not in self._possible_ways:
            self._possible_ways.add(way)
            self._queue.put(way)

    def move_next(self) -> bool:
        return len(self._possible_ways) > 0

    def current(self) -> int:
        way = self._queue.get()
        self._possible_ways.remove(way)
        return way


def is_pony(string: str, bor: {}) -> bool:
    state = State()
    state.add(0)
    while state.move_next():
        start = state.current()
        if check_string(string, bor, start, state):
            return True
    return False


def check_string(string: str, tree: dict, start: int, state: State) -> bool:
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


def add_word(tree: {}, word: str):
    node = tree
    for letter in word:
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
