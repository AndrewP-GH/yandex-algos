import sys


def main():
    s = input().split()
    n, k = int(s[0]), int(s[1])
    houses = [int(x) for x in sys.stdin.readline().rstrip().split()]
    s_h = sorted(houses)
    count = 0
    for i in range(n):
        k -= s_h[i]
        count += 1
        if k == 0:
            return count
        elif k < 0:
            return count - 1 if count > 0 else 0
    return count


print(main())

