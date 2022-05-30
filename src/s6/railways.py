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
    return n, graph


def is_optimal(graph, n):
    visited = ['W'] * n
    for city in range(n):
        if visited[city] != 'W':
            continue
        stack = [city]
        while len(stack) > 0:
            current = stack[-1]
            if visited[current] == 'W':
                visited[current] = 'G'
                for target in graph[current]:
                    if visited[target] == 'W':
                        stack.append(target)
                    elif visited[target] == 'G':
                        return False
            else:
                visited[current] = 'B'
                stack.pop()
    return True


if __name__ == '__main__':
    _n, _graph = init()
    if is_optimal(_graph, _n):
        print('YES')
    else:
        print('NO')
