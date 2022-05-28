import sys
from collections import defaultdict


def max_distance(edges, n, s):
    color = [False] * (n + 1)
    distance = [0] * (n + 1)
    planned = []
    color[s] = True
    distance[s] = 0
    planned.append(s)
    while len(planned) > 0:
        v = planned.pop(0)
        for u in edges[v]:
            if not color[u]:
                color[u] = True
                distance[u] = distance[v] + 1
                planned.append(u)
    max_dist = max(distance)
    print(max_dist)


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
        edges[v].append(u)
    s = int(sys.stdin.readline())
    max_distance(edges, n, s)
