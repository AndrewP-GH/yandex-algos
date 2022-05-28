from collections import defaultdict
from enum import Enum


class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3


def main_dfs(edges, s):
    colors = [Color.WHITE] * (n + 1)
    entry = [None] * (n + 1)
    leave = [None] * (n + 1)
    dfs(edges, s, colors, entry, leave)
    return entry, leave


def dfs(edges, s, colors, entry, leave):
    time = 0
    stack = [s]
    while len(stack) > 0:
        v = stack.pop()
        if colors[v] == Color.WHITE:
            entry[v] = time
            colors[v] = Color.GRAY
            stack.append(v)
            time += 1
            for w in edges[v]:
                if colors[w] == Color.WHITE:
                    stack.append(w)
        elif colors[v] == Color.GRAY:
            leave[v] = time
            colors[v] = Color.BLACK
            time += 1


if __name__ == '__main__':
    line = input().split()
    n = int(line[0])
    m = int(line[1])
    edges = defaultdict(list)
    for _ in range(m):
        line = input().split()
        u = int(line[0])
        v = int(line[1])
        edges[u].append(v)
    for key in edges.keys():
        edges[key].sort(reverse=True)
    entry, leave = main_dfs(edges, 1)
    for i in range(1, n + 1):
        print(entry[i], leave[i])
