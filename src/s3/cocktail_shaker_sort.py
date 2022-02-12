def main():
    array = [5, 4, 3, 2, 1]
    cocktail_shaker_sort(array)
    print(array)


def cocktail_shaker_sort(array):
    left = 0
    right = len(array) - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(left, right, 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        right -= 1
        if not swapped:
            break
        swapped = False
        for i in range(right, left, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True
        left += 1


if __name__ == '__main__':
    main()
