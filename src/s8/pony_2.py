# Отчет 69245683: https://contest.yandex.ru/contest/26133/run-report/69245683/
# Алгоритм работы:
# 1. Читать слово и добавлять его в бор (префиксное дерево) задом наперёд. За узел дерева берем словарь,
#   а в нём помещаем в ключе end_word_marker значение True, если данное слово заканчивается в текущем узле дерева.
# 2. Воспользуемся динамическим программированием для проверки, можно ли составить слово из тех, что у нас в боре.
#   Заведем булевый массив dp длины n=len(проверяемая_строка)+1. В нём будем хранить информацию о том, можно ли
#   построить слово из тех, что у нас в боре. dp[0] установим в True, а True в dp[i] будет указывать на то, что
#   подстроку [0, i) можно составить из слов в боре.
# 3. Тогда ответ для всей строки будет в dp[n]. Чтобы вычислить все значения в массиве dp, будем идти по исходной строке
#   слева направо. Для каждого символа в строке будем проверять, находится ли он в руте бора, и если да, проверяем
#   символы перед ним j = (i-1, i-2, ..., 0), есть ли они далее в боре.
# 4. Если при этом мы встречаем узел, в котором находится символ конца слова, проверяем, есть ли в массиве dp значение
#   True для индекса j текущей буквы в слова. Если да, то мы можем построить слово. Если нет, то мы проверяем подстроку
#   дальше.
#
# Cложность алгоритма:
# n - для проверяемой строки, m - средняя длина слова в боре, k - количество слов в боре.
# Время работы: O(n) в среднем и O(n^2) в худшем (например, строка aaaa и бор букв а, а, а, а, а) для проверки слова
#   с помощью динамического программирования, т.к. каждую букву слова можно проверить за O(1),
#   и O(k*m) на составление бора.
#   Итоговая алгоритмическая сложность: O(n + k*m) в среднем и O(n^2 + k*m) в худшем случае.
# Память: O(n + k*m) - для хранения строки, бора и массива dp.

import sys
import unittest

end_word_marker = '$'


def is_pony(string: str, bor: {}) -> bool:
    l_s = len(string)
    dp = [False] * (l_s + 1)
    dp[0] = True
    for i in range(l_s):
        j = i
        node = bor
        while j >= 0:
            letter = string[j]
            node = node.get(letter)
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
