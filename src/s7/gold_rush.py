import sys


def gold_rush(pack, n, values):
    values = sorted(values, reverse=True)
    gain = 0
    i = 0
    while i < n and pack > 0:
        c, m = values[i]
        if pack > m:
            pack -= m
            gain += c * m
        else:
            gain += c * pack
            pack = 0
        i += 1
    return gain


if __name__ == '__main__':
    _M = int(input())
    _n = int(input())
    _values = [None] * _n
    for _i in range(_n):
        _c, _m = map(int, sys.stdin.readline().split())
        _values[_i] = (_c, _m)
    print(gold_rush(_M, _n, _values))
