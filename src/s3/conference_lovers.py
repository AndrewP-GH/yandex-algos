from collections import defaultdict


def main():
    n = int(input())
    ids = input().split()
    k = int(input())
    d = defaultdict(int)
    for i in ids:
        d[i] += 1
    top = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return map(lambda item: item[0], top[:k])


if __name__ == '__main__':
    print(*main())
