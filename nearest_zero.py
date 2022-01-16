# ID 63940476

import sys


def main():
    n = int(input())
    line = sys.stdin.readline().split()
    result = [n] * n
    begin = 0
    for i in range(n):
        if line[i] == '0':
            fill_left(i, begin, result)
            begin = i
    end = n - 1
    for j in range(n - 1, -1, -1):
        if line[j] == '0':
            fill_right(j, end, result)
            end = j
    return result


def fill_left(i, begin, result):
    distance = 0
    while i >= begin:
        if result[i] >= distance:
            result[i] = distance
            distance += 1
            i -= 1
        else:
            break


def fill_right(i, end, result):
    distance = 0
    while i <= end:
        if result[i] >= distance:
            result[i] = distance
            distance += 1
            i += 1
        else:
            break


if __name__ == '__main__':
    arr = main()
    print(' '.join(map(str, arr)))  # с *arr на 0.3s медленнее :(
