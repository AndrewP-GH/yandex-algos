import sys


def difference_of_trash_indexes(n, numbers, k):
    numbers = sorted(numbers)
    low_diff = 0
    for i in range(n - 1):
        low_diff = min(low_diff, numbers[i + 1] - numbers[i])
    high_diff = numbers[n - 1] - numbers[0]
    while low_diff < high_diff:
        mid_diff = (low_diff + high_diff) // 2
        if count_pairs(numbers, n, mid_diff) < k:
            low_diff = mid_diff + 1
        else:
            high_diff = mid_diff
    return low_diff


def count_pairs(numbers, n, diff):
    count = 0
    for i in range(n):
        count += upper_bound(numbers, n, numbers[i] + diff) - i - 1
    return count


def upper_bound(numbers, n, diff):
    low, high = 0, n
    while low < high:
        mid = (low + high) // 2
        if numbers[mid] <= diff:
            low = mid + 1
        else:
            high = mid
    return low


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    k = int(input())
    result = difference_of_trash_indexes(n, numbers, k)
    print(result)
