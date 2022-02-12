def main():
    array = [5, 4, 3, 2, 1]
    cocktail_shaker_sort(array)
    print(array)


def cocktail_shaker_sort(array):
    left = 0
    right = len(array) - 1
    control = right
    while left < right:
        for i in range(left, right, 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                control = i
        right = control
        for i in range(right, left, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                control = i
        left = control


if __name__ == '__main__':
    main()
