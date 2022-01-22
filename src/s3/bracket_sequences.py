import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    gen(n)


def gen(n, s='', left=0, right=0):
    if left == n and right == n:
        return print(s)
    if left < n:
        gen(n, s + '(', left + 1, right)
    if left > right:
        gen(n, s + ')', left, right + 1)


if __name__ == '__main__':
    main()
