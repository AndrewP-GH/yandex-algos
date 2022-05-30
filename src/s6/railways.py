from collections import defaultdict
from sys import stdin


def init():
    n = int(stdin.readline())
    graph = defaultdict(list)
    for i in range(n):
        city = i
        line = stdin.readline().rstrip()
        for j in range(len(line)):
            target = city + j + 1
            if line[j] == 'R':
                graph[city].append(target)
            else:
                graph[target].append(city)
    for k in graph.keys():
        graph[k] = sorted(graph[k], reverse=True)
    return n, graph


def is_optimal(graph, n):
    railways = [None] * n
    for i in range(n):
        railways[i] = set()
    for start in range(n):
        visited = [False] * n
        planned = [start]
        visited[start] = True
        while len(planned) > 0:
            current = planned.pop()
            if start in railways[current]:
                return False
            for end in graph[current]:
                if not visited[end]:
                    railways[start].add(end)
                    planned.append(end)
                    visited[end] = True
    return True


if __name__ == '__main__':
    _n, _graph = init()
    if is_optimal(_graph, _n):
        print('YES')
    else:
        print('NO')
