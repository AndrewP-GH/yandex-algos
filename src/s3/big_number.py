import functools
import sys


def comparer(left, right):
    f = int(left + right)
    b = int(right + left)
    if f > b:
        return -1
    elif f == b:
        return 0
    else:
        return 1


class YourTupleComparator(tuple):  # alternative for functools.cmp_to_key
    def __lt__(self, other):
        return comparer(*self, *other)  # or comparer(self[0], other[0])


def main():
    n = int(input())
    numbers = sys.stdin.readline().rstrip().split()
    return sorted(numbers, key=functools.cmp_to_key(comparer))
    # return sorted(numbers, key=YourTupleComparator)


if __name__ == '__main__':
    print(''.join(map(str, main())))
