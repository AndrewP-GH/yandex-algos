import sys
from collections import defaultdict


def bfs(edges, n, s):
    queue = [None] * n
    count = 0
    color = [False] * (n + 1)
    planned = []
    color[s] = True
    planned.append(s)
    while len(planned) > 0:
        v = planned.pop(0)
        queue[count] = v
        count += 1
        for u in sorted(edges[v]):
            if not color[u]:
                color[u] = True
                planned.append(u)
    print(" ".join(map(str, queue[:count])))


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
    bfs(edges, n, s)
