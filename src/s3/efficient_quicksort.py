# 66071156 https://contest.yandex.ru/contest/23815/run-report/66071156/
# Алгоритм работы сортировки:
# 1. Для выбора опорного элемента и сортировки используем схему Хоара
# - берем средний элемент
# - идем с начала и конца по массиву и переставляем элементы так, чтобы те, которые меньше опорного оказались слева от него,
# а те, что больше, спарва от него
# 2. Применяем сортировку к левому и правому подмассивам
import sys


def efficient_quicksort(array, left, right, comparator):
    if right - left < 1:
        return
    pivot_idx = partition(array, left, right, comparator)
    efficient_quicksort(array, left, pivot_idx, comparator)
    efficient_quicksort(array, pivot_idx + 1, right, comparator)


def partition(array, left, right, comparator):
    mid_idx = (left + right) // 2
    pivot = array[mid_idx]
    while True:
        while comparator(array[left], pivot):
            left += 1
        while comparator(pivot, array[right]):
            right -= 1
        if left >= right:
            return right
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1


def compare(left, right):
    if left[1] != right[1]:
        return left[1] > right[1]
    if left[2] != right[2]:
        return left[2] < right[2]
    return left[0] < right[0]


if __name__ == "__main__":
    number = int(input())
    participants = [None] * number
    for i in range(number):
        parts = sys.stdin.readline().rstrip().split()
        participants[i] = (parts[0], int(parts[1]), int(parts[2]))
    efficient_quicksort(participants, 0, number - 1, compare)
    for p in participants:
        print(p[0])
