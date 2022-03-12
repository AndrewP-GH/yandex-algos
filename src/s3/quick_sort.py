def quick_cort(numbers):
    if len(numbers) < 2:
        return numbers
    n = len(numbers)
    pivot = sorted([numbers[0], numbers[n // 2], numbers[n - 1]])[1]
    left, center, right = partition(numbers, pivot)
    return quick_cort(left) + center + quick_cort(right)


def partition(numbers, pivot):
    left = []
    center = []
    right = []
    for numb in numbers:
        if numb < pivot:
            left.append(numb)
        elif numb > pivot:
            right.append(numb)
        else:
            center.append(numb)
    return left, center, right


if __name__ == '__main__':
    array = [3, 7, 9, 14, 1, 2, 5]
    res = quick_cort(array)
    print(res)
