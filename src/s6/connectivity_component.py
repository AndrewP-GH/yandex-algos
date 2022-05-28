import sys
from collections import defaultdict


def dfs(edges, s, color, component, components):
    stack = [s]
    while len(stack) > 0:
        s = stack.pop()
        if color[s] != -1:
            continue
        color[s] = component
        components[component].append(s)
        for v in edges[s]:
            if color[v] == -1:
                stack.append(v)


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
    for key in edges.keys():
        edges[key].sort(reverse=True)
    color = [-1] * (n + 1)
    component_count = 0
    components = defaultdict(list)
    for i in range(1, n + 1):
        if color[i] == -1:
            component_count += 1
            dfs(edges, i, color, component_count, components)
    print(component_count)
    for component in sorted(components.keys()):
        sorted_component = sorted(components[component])
        print(" ".join(map(str, sorted_component)))
