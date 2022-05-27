# Отчет https://contest.yandex.ru/contest/24810/run-report/68628116/
#
# Сортировка состоит из 2-ч частей:
# 1. Вставляю в max-кучу
# 2. Достаю из max-кучи
#
# Для сравнения участников реализован класс Participant с методом сравнения "<".
#
# В качестве реализации кучи взял простой массив с отдельным параметром "размер", чтобы избегать лишних аллокаций.
#
# Сложность по памяти O(n*m). Фактически 3*n*m - начальные данные, куча, результат, где n - число участников (строка и
#   2 числа), m - размер строки с именем.
#
# В реализации алгоритма память под массивы выделяется заранее, поэтому доп аллокаций во время итераций не происходит и
#   на итоговую сложность они не оказывают влияния.
#
# Сложность по времени O(n*log(n)):
# - вставка в кучу: O(log(n)) (здесь и далее я не учитываю сложность сравнения строк, потому что это поле используется
#   последним в списке сравнения),
# - извлечение из кучи: O(log(n)),
# - эти операции надо выполнить над каждым элементом входного массива, получаем O(2n*log(n)) -> O(n*log(n))#

import sys


class Participant:
    def __init__(self, name, tasks, fine):
        self.name = name
        self.tasks = tasks
        self.fine = fine

    def __lt__(self, other):
        if self.tasks != other.tasks:
            return self.tasks < other.tasks
        if self.fine != other.fine:
            return self.fine > other.fine
        return self.name > other.name


class Heap:
    def __init__(self, array, size):
        self.array = array
        self.size = size

    def __getitem__(self, idx):
        return self.array[idx]

    def __setitem__(self, idx, value):
        self.array[idx] = value

    def __len__(self):
        return self.size


def heapsort(arr):
    heap_length = len(arr) + 1
    heap_array = [None] * heap_length
    heap = Heap(heap_array, 1)
    for item in arr:
        heap_add(heap, item)
    sorted_array = [None] * len(arr)
    for i in range(len(arr)):
        result = heap_get_max_priority(heap)
        sorted_array[i] = result
    return sorted_array


def heap_add(heap: Heap, item):
    index = heap.size
    heap[index] = item
    heap.size += 1
    sift_up(heap, index)


def sift_up(heap: [], idx):
    def parent_idx(i):
        return i // 2

    parent = parent_idx(idx)
    while idx > 1 and heap[parent] < heap[idx]:
        heap[parent], heap[idx] = heap[idx], heap[parent]
        idx = parent
        parent = parent_idx(idx)
    return idx


def heap_get_max_priority(heap: Heap):
    result = heap[1]
    heap[1] = heap[heap.size - 1]
    heap.size -= 1
    sift_down(heap, 1)
    return result


def sift_down(heap: Heap, idx):
    def children_idx(i):
        return i * 2, i * 2 + 1

    left, right = children_idx(idx)
    while heap.size > left:
        if right < heap.size and heap[left] < heap[right]:
            largest = right
        else:
            largest = left
        if heap[idx] < heap[largest]:
            heap[idx], heap[largest] = heap[largest], heap[idx]
        idx = largest
        left, right = children_idx(idx)
    return idx


if __name__ == '__main__':
    n = int(input())
    participants = [None] * n
    for row in range(n):
        line = sys.stdin.readline().rstrip().split()
        participants[row] = Participant(line[0], int(line[1]), int(line[2]))
    winners = heapsort(participants)
    for participant in winners:
        print(participant.name)
