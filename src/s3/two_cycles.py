import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    numbers = [int(x) for x in sys.stdin.readline().rstrip().split()]
    s = int(sys.stdin.readline().rstrip())
    print(find_left(n, numbers, s), find_left(n, numbers, s * 2))


def find_left(n, numbers, s):
    left = 0
    high = n
    while left < high:
        mid = left + (high - left) // 2
        if numbers[mid] >= s:
            high = mid
        else:
            left = mid + 1
    if 0 <= left < n and numbers[left] >= s:
        return left + 1
    else:
        return -1


if __name__ == '__main__':
    main()
