# 65983139 https://contest.yandex.ru/contest/23815/run-report/65983139/
# Алгоритм работает следующим образом:
# 1. Бинарным поиском ищем правую границу "сдвинутого" массива (самый большой элемент),
# 2. Если не нашли (-1) -> значит это просто отсортированный массив и ищем в нем обычным бинарным поиском
# 3. Если нашли -> проверяем не искомый ли это элемент,
# 4. Если нет -> проверяем левую границу, чтобы понят, в каком из двух подмассивов надо искать
# 5. Ищем в нужном подмассиве бинарным поиском.
# Оценка сложности:
# функция find_pivot имеет в среднем и худшем случаях сложность O(log(n)),
# потому что это операция "бинарного поиска" (каждый раз делим пополам) и O(1) в лучшем;
# функция broken_search в худшем и среднем случае имеет сложность O(log(n)), в лучшем случае O(1),
# поэтому итоговая сложность алгоритма O(log(n)).
from bisect import bisect_left


def broken_search(nums, target) -> int:
    n = len(nums)
    pivot = find_pivot(nums, 0, n - 1)
    if pivot == -1:
        return binary_search(nums, target, 0, n - 1)
    if nums[pivot] == target:
        return pivot
    if nums[0] <= target:
        return binary_search(nums, target, 0, pivot - 1)
    return binary_search(nums, target, pivot + 1, n - 1)


def binary_search(array, target, low, high):
    result = bisect_left(array, target, low, high)
    if result != len(array) and array[result] == target:
        return result
    return -1


def find_pivot(array, low, high) -> int:
    if array[low] < array[high]:
        return -1
    while low < high:
        mid = (low + high) // 2
        if mid < high and array[mid] > array[mid + 1]:  # проверяем на границы, прежде чем сравнивать с +1
            return mid
        if mid > low and array[mid] < array[mid - 1]:  # проверяем на границы, прежде чем сравнивать с -1
            return mid - 1
        if array[low] >= array[mid]:
            high = mid - 1
        elif array[mid] >= array[high]:
            low = mid + 1
    return low


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == "__main__":
    test()
