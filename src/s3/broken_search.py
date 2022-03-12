# 65983139 https://contest.yandex.ru/contest/23815/run-report/65983139/
# Алгоритм работает следующим образом:
# 1. Бинарным поиском ищем правую границу "сдвинутого" массива (самый большой элемент),
# 2. Если не нашли (-1) -> значит это просто отсортированный массив и ищем в нем обычным бинарным поиском
# 3. Если нашли -> проверяем не искомый ли это элемент,
# 4. Если нет -> проверяем левую границу, чтобы понят, в каком из двух подмассивов надо искать
# 5. Ищем в нужном подмассиве бинарным поиском.

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


def find_pivot(array, low, high) -> int:
    if high < low:
        return -1
    if high == low:
        return low
    mid = (low + high) // 2
    if mid < high and array[mid] > array[mid + 1]:
        return mid
    if mid > low and array[mid] < array[mid - 1]:
        return mid - 1
    if array[low] >= array[mid]:
        return find_pivot(array, low, mid - 1)
    if array[mid] >= array[high]:
        return find_pivot(array, mid + 1, high)
    return -1


def binary_search(array, target, low, high):
    if high < low:
        return -1
    mid = (low + high) // 2
    if array[mid] == target:
        return mid
    if array[mid] > target:
        return binary_search(array, target, low, mid - 1)
    return binary_search(array, target, mid + 1, high)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == "__main__":
    test()
