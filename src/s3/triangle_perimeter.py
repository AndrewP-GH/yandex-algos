import sys


def main():
    n = int(input())
    numbers = [int(x) for x in sys.stdin.readline().rstrip().split()]
    sorted_numbers = sorted(numbers, reverse=True)
    for i in range(n-2):
        j = i+1
        while j < n - 1:
            c = sorted_numbers[i]
            a_and_b = sorted_numbers[j] + sorted_numbers[j+1]
            if c < a_and_b:
                return c + a_and_b
            j += 1
    return None


if __name__ == '__main__':
    print(main())
