def main():
    array = [11, 2, 9, 7, 1]
    for i in range(1, len(array)):
        item = array[i]
        j = i
        while j > 0 and item < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        array[j] = item
        print(f'Step: {i}, array: {array}')


if __name__ == '__main__':
    main()
