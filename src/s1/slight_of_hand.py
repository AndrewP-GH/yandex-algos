# ID 63940599

import sys
from collections import defaultdict


def main():
    k = int(input())
    field_stat = defaultdict(int)
    for row in range(4):
        line = sys.stdin.readline().rstrip()
        for ch in line:
            field_stat[ch] += 1
    kk = 2*k
    points = 0
    for k, v in field_stat.items():
        if k != '.' and v <= kk:
            points += 1
    return points


if __name__ == '__main__':
    res = main()
    print(res)
