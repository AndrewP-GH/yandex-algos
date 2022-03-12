import sys


def partial_sort(n, numbers):
    buckets = 0
    local_max = 0
    for i in range(0, n):
        number = numbers[i]
        all_more = True
        for j in range(i + 1, n):
            all_more &= number < numbers[j] and local_max < numbers[j]
            if not all_more:
                break
        if all_more or i == n - 1:
            buckets += 1
        local_max = max(local_max, number)
    return buckets


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    result = partial_sort(n, numbers)
    print(result)
