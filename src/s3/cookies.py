import sys


def main():
    n = int(sys.stdin.readline())
    greed_factor = [int(x) for x in sys.stdin.readline().rstrip().split()]
    m = int(sys.stdin.readline())
    cookies = [int(x) for x in sys.stdin.readline().rstrip().split()]
    happy_children = 0
    s_g = sorted(greed_factor)
    s_c = sorted(cookies)
    i, j = 0, 0
    while i < n and j < m:
        if s_g[i] <= s_c[j]:
            happy_children += 1
            i += 1
        j += 1
    return happy_children


print(main())
