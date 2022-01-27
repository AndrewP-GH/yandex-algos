def main():
    array = [8, 5, 2, 6, 9, 3, 1, 2, 4, 0, 7]
    for i in range(len(array) - 1):
        min_i = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_i]:
                min_i = j
        array[i], array[min_i] = array[min_i], array[i]
        print(array)


if __name__ == '__main__':
    main()
