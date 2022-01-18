import sys


def main():
    n, k = [int(x) for x in sys.stdin.readline().split()]
    i_2 = 1
    i_1 = 1
    mod = 10 ** k
    if n in (0, 1):
        return 1 % mod
    for _ in range(n - 1):
        res = (i_2 + i_1) % mod
        i_2 = i_1
        i_1 = res
    return i_1


if __name__ == '__main__':
    print(main())
