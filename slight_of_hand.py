# ID 63937226

import sys


def main():
    k = int(input())
    field_stat = {}
    for row in range(0, 4):
        line = sys.stdin.readline()
        for col in range(0, 4):
            n = line[col]
            field_stat[n] = field_stat.get(n, 0) + 1
    kk = 2*k
    points = 0
    for k, v in field_stat.items():
        if k != '.' and v <= kk:
            points += 1
    return points


if __name__ == '__main__':
    res = main()
    print(res)
