import sys


def main():
    n = int(sys.stdin.readline())
    numbers = [int(x) for x in sys.stdin.readline().rstrip().split()]
    already_sorted = True
    for i in range(n-1):
        flag = False
        for j in range(1, n-i):
            if numbers[j - 1] > numbers[j]:
                numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
                flag = True
                already_sorted = False
        if flag:
            print(*numbers)
        else:
            if already_sorted:
                print(*numbers)
            return


if __name__ == '__main__':
    main()
