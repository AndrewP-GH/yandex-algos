# Отчет 69049769: https://contest.yandex.ru/contest/25597/run-report/69049769/
# Алгоритм работы:
#   Задача представляет собой вариацию задачи о рюкзаке, где необходимо проверить, можно ли добиться максимального веса
# из предложенных вещей.
#   Используем динамическое программирование:
# 1. Возьмем сумму всех элементов и делим на 2, если она делится с остатком, то разбияния из целых чисел нет, иначе –
# заведем булевый массив из двух строк, причем длина строки будет равна половине суммы всех элементов + 1, при этом
# индекс колонки будет соответствовать сумме, которую можно получить, сложив изначальные числа.
# 2. Изначально строки заполнены значением False.
# 3. При переходе динамики мы будем последовательно рассматривать каждое число в изначальном массиве и заполнять наш
# массив значением True, если соответствующую сумму можно получить, используя это число, число равно сумме, либо на
# предыдущем шаге, возможно, у нас была получена сумма, равная current_sum - number, либо мы уже получали эту сумму на
# предыдущем шаге, иначе оставляем False.
# 4. Будем идти от меньшей сумме к большей (слева направо).
# 5. Если мы заполнили последний символ в строке значением True, значит такое разбиение есть.
#
#   Пусть получумма элементов в массиве размером M равна N, тогда
# алгоритмическая сложность равна O(M*N),
# сложность по памяти равна O(N).
#
#   Также можно было бы применить оптимизацию, проверяя, есть ли в массиве элемент больше получуммы, в таком случае
# запускать алгоритм не имеет смысла и можно сразу вернуть False.

import sys
import unittest


def same_amounts(numbers: [int]) -> bool:
    if len(numbers) < 2:
        return False
    total = sum(numbers)
    if total % 2 != 0:
        return False
    target = total // 2
    row_width = target + 1
    dp = [[False] * row_width for _ in range(2)]
    current_row = 1
    previous_row = 0
    for number in numbers:
        for sub_sum in range(row_width):
            if sub_sum < number:
                dp[current_row][sub_sum] = dp[previous_row][sub_sum]
            elif sub_sum == number:
                dp[current_row][sub_sum] = True
            else:
                dp[current_row][sub_sum] = dp[previous_row][sub_sum] or dp[previous_row][sub_sum - number]
        if dp[current_row][target]:
            return True
        current_row, previous_row = current_row ^ 1, current_row
    return False


if __name__ == '__main__':
    _n = sys.stdin.readline()
    _numbers = [int(x) for x in sys.stdin.readline().split()]
    _res = same_amounts(_numbers)
    print(_res)


class Tests(unittest.TestCase):
    def test_first(self):
        numbers = [1, 5, 7, 1]
        expected = True
        self.assertEqual(same_amounts(numbers), expected)

    def test_seconf(self):
        numbers = [2, 10, 9]
        expected = False
        self.assertEqual(same_amounts(numbers), expected)

    def test_third(self):
        numbers = [4]
        expected = False
        self.assertEqual(same_amounts(numbers), expected)

    def test_fourth(self):
        numbers = [7, 9, 3, 4, 6, 7]
        expected = True
        self.assertEqual(same_amounts(numbers), expected)
