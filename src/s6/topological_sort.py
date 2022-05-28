import sys
from collections import defaultdict
from enum import Enum


class Color(Enum):
    WHITE = 0,
    GRAY = 1,
    BLACK = 2


def top_sort(edges, s, entry, result):
    entry[s] = Color.GRAY
    for v in edges[s]:
        if entry[v] == Color.WHITE:
            top_sort(edges, v, entry, result)
    entry[s] = Color.BLACK
    result.append(s)


if __name__ == '__main__':
    line = sys.stdin.readline().split()
    n = int(line[0])
    m = int(line[1])
    edges = defaultdict(list)
    for _ in range(m):
        line = sys.stdin.readline().split()
        u = int(line[0])
        v = int(line[1])
        edges[u].append(v)
    for key in edges.keys():
        edges[key].sort(reverse=True)
    entry = [Color.WHITE] * (n + 1)
    order = []
    for i in range(1, n + 1):
        if entry[i] is Color.WHITE:
            top_sort(edges, i, entry, order)
    order.reverse()
    print(" ".join(map(str, order)))
