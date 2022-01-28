import sys


def main():
    n = int(input())
    colors = sys.stdin.readline().rstrip().split()
    low = 0  # first 1
    mid = 0  # current
    high = n - 1  # 'first' 2
    while mid <= high:
        if colors[mid] == '0':
            colors[low], colors[mid] = colors[mid], colors[low]
            low += 1
            mid += 1
        elif colors[mid] == '1':
            mid += 1
        else:
            colors[high], colors[mid] = colors[mid], colors[high]
            high -= 1
    return colors


if __name__ == '__main__':
    print(*main())
