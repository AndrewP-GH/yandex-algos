import sys
from collections import defaultdict, deque


def init():
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
    for k in edges.keys():
        edges[k] = sorted(edges[k])
    s = int(sys.stdin.readline())
    return edges, n, s


def bfs(edges, n, s):
    queue = [None] * n
    count = 0
    color = [False] * (n + 1)
    color[s] = True
    planned = deque([s])
    while len(planned) > 0:
        v = planned.popleft()
        queue[count] = v
        count += 1
        for u in edges[v]:
            if not color[u]:
                color[u] = True
                planned.append(u)
    print(" ".join(map(str, queue[:count])))


if __name__ == '__main__':
    edges, n, s = init()
    bfs(edges, n, s)
