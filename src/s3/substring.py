import sys


def main():
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()
    return find(s, t)


def find(s, t):
    m, n = 0, 0
    while m < len(s) and n < len(t):
        if s[m] == t[n]:
            m += 1
        n += 1
    return m == len(s)


print(main())
