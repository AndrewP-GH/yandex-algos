import sys


def hobby_groups():
    n = int(input())
    known = set()
    for i in range(n):
        name = sys.stdin.readline().rstrip()
        if name in known:
            continue
        known.add(name)
        print(name)


if __name__ == '__main__':
    hobby_groups()
