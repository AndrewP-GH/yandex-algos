import sys
from collections import defaultdict


def four_sum():
    n = int(input())
    if n < 4:
        print(0)
        return
    s = int(input())
    numbers = [int(x) for x in sys.stdin.readline().rstrip().split()]
    result = set()
    known_sums = defaultdict(list)
    known_sums[numbers[0] + numbers[1]].append((numbers[0], numbers[1]))
    for i in range(2, n - 1):
        for j in range(i + 1, n):
            r_1, r_2 = numbers[i], numbers[j]
            need_sum = s - r_1 - r_2
            if need_sum in known_sums:
                for l_1, l_2 in known_sums[need_sum]:
                    result.add(tuple(sorted((l_1, l_2, r_1, r_2))))
        for j in range(0, i):
            known_sums[numbers[i] + numbers[j]].append((numbers[i], numbers[j]))
    print(len(result))
    for r in sorted(result):
        print(' '.join(map(str, r)))


if __name__ == '__main__':
    four_sum()
