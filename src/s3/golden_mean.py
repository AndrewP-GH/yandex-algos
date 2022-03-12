import sys


def golden_mean(n, m, north, south):
    total = n + m
    middle = total // 2
    north_counter, south_counter = 0, 0
    current, prev = None, None
    for i in range(middle + 1):
        prev = current
        if north_counter >= n:
            current = south[south_counter]
            south_counter += 1
        elif south_counter >= m:
            current = north[north_counter]
            north_counter += 1
        elif north[north_counter] <= south[south_counter]:
            current = north[north_counter]
            north_counter += 1
        else:
            current = south[south_counter]
            south_counter += 1
    return current if total % 2 != 0 else (current + prev) / 2


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    north = list(map(int, sys.stdin.readline().rstrip().split()))
    south = list(map(int, sys.stdin.readline().rstrip().split()))
    result = golden_mean(n, m, north, south)
    print(result)
