# 66144262 https://contest.yandex.ru/contest/23815/run-report/66144262/
# Алгоритм работы сортировки:
# 1. Для выбора опорного элемента и сортировки используем схему Хоара
# - берем средний элемент
# - идем с начала и конца по массиву и переставляем элементы так, чтобы те, которые меньше опорного оказались слева,
# а те, что больше, справа от него
# 2. Применяем сортировку к левому и правому подмассивам
# Сложность:
# Функция partition работает за O(n) и не требует дополнительной памяти
# Поэтому функция efficient_quicksort работает за O(n*log n): на каждом шаге рекурсии мы вызываем функцию partition,
# делим массив на 2 подмассива и вызываем efficient_quicksort на них.
# В худшем случае, если массив отсортирован по возрастанию, будет n вызовов функции partition O(n) и итоговая
# сложност будет O(n^2)
# Сложность по памяти: дополнительной памяти (кроме памяти под сам массив) не требуется, поэтому она равна O(1).
import sys


def efficient_quicksort(array, left, right):
    if right - left < 1:
        return
    pivot_idx = partition(array, left, right)
    efficient_quicksort(array, left, pivot_idx)
    efficient_quicksort(array, pivot_idx + 1, right)


def partition(array, left, right):
    mid_idx = (left + right) // 2
    pivot = array[mid_idx]
    while True:
        while array[left] < pivot:
            left += 1
        while pivot < array[right]:
            right -= 1
        if left >= right:
            return right
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1


class Intern:
    def __init__(self, login, tasks, fine):
        self.login = login
        self.tasks = tasks
        self.fine = fine

    def __lt__(self, other):
        if self.tasks != other.tasks:
            return self.tasks > other.tasks
        if self.fine != other.fine:
            return self.fine < other.fine
        return self.login < other.login


if __name__ == "__main__":
    number = int(input())
    participants = [Intern] * number
    for i in range(number):
        parts = sys.stdin.readline().rstrip().split()
        participants[i] = Intern(parts[0], int(parts[1]), int(parts[2]))
    efficient_quicksort(participants, 0, number - 1)
    for p in participants:
        print(p.login)
