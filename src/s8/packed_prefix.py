# Отчет: 69250190 https://contest.yandex.ru/contest/26133/run-report/69250190/
# Алгоритм работы:
# 1. Распакаовка строк
# 2. Поиск максимального префикса
#   Первый этап происходит с помощью стека и метода грацин — дабавляем все "не скобки" в стек, а как только встречается
# закрывающая скобка, собираем выражение внутри нее в одну строку и кладем обратно на стек. Когда всю строку подобрын
# образом обработали, собираем итоговый результат, раскручивкая стек.
#   На втором этапе простым сравнением символов строк на соответствующих позициях ищем общий префикс.
#
# Алгоритмическая сложнсоть:
#   Первый этап обработки 1 строки занимает O(N) в среднем и O(N^2) в худщем случае, где N — длина строки.
# Худший случай - 1[a]1[b]1[c]..., т.е. когда мы каждый четвертый символ вынуждены раскручяивать стек, в этом случае
# будет O(n*n/4) операций.
#   На самом деле, тут еще стоит учитывая сложность операции конкатенаци двух строк, а она будет O(n+m), где n — длина
# первой строки, m — длина второй строки. Т.е. на самом деле алгоритма будет работать за O(Nm), где m - средняя длинна
# строки и m<N, к которой мы будем добавлять символ(ы) в начало.
#   Итоговая сложность этого этапа будет O(NmK) в среднем и O(K*N^2) в худщем случае, где k - кол-во строк на распаковку.
#   На втором этапе за линейное время O(N) проверяем по очереди перваые символы всех строк на соответствие.
# Итоговая — O(NmK) в среднем и O(K*N^2) в худщем случае.
#
# Пространственная сложность:
#   Первый этап обработки 1 строки занимает O(N) (под стек с промежуточными данными). Посколько строки обрабатываются по
# очереди, итоговая так же будет O(N+l), где l — длина строки c результатом.

import sys
import unittest


def packed_prefix(n, lines):
    template = lines[0]
    for i in range(len(template)):
        ch = template[i]
        for j in range(1, n):
            line = lines[j]
            if i > len(line) or line[i] != ch:
                return template[:i]
    return template


def unpack(line):
    stack = []
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == ']':
            top = stack.pop()
            local = ""
            while not top.isnumeric():
                local = top + local
                top = stack.pop()
            local = int(top) * local
            stack.append(local)
        elif ch != '[':
            stack.append(ch)
        i += 1

    result = ""
    while len(stack) > 0:
        result = stack.pop() + result
    return result


if __name__ == '__main__':
    _n = int(input())
    _lines = [None] * _n
    for _i in range(_n):
        _line = sys.stdin.readline().rstrip()
        _lines[_i] = unpack(_line)
    print(packed_prefix(_n, _lines))


class TestPackedPrefix(unittest.TestCase):
    def test_unpack_line_1(self):
        line = '2[a]2[ab]'
        exp = 'aaabab'
        self.assertEqual(unpack(line), exp)

    def test_unpack_line_2(self):
        line = '3[a]2[r2[t]]'
        exp = 'aaarttrtt'
        self.assertEqual(unpack(line), exp)

    def test_unpack_line_3(self):
        line = 'a2[aa3[b]]'
        exp = 'aaabbbaabbb'
        self.assertEqual(unpack(line), exp)

    def test_unpack_line_4(self):
        line = '2[abac]a'
        exp = 'abacabaca'
        self.assertEqual(unpack(line), exp)

    def test_unpack_line_5(self):
        line = '3[aba]'
        exp = 'abaabaaba'
        self.assertEqual(unpack(line), exp)

    def test_unpack_line_6(self):
        line = '3[aba]c'
        exp = 'abaabaabac'
        self.assertEqual(unpack(line), exp)

    def test_max_prefix_1(self):
        n = 3
        lines = ['aaabab', 'aaarttrtt', 'aaabbbaabbb']
        exp = 'aaa'
        self.assertEqual(packed_prefix(n, lines), exp)

    def test_max_prefix_2(self):
        n = 3
        lines = ['abacabaca', 'abacabaca', 'abaabaaba']
        exp = 'aba'
        self.assertEqual(packed_prefix(n, lines), exp)
