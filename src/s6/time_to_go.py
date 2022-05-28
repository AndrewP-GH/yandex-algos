from collections import defaultdict


def main_dfs(edges, s):
    processed = [None] * (n + 1)
    entry = [None] * (n + 1)
    leave = [None] * (n + 1)
    dfs(edges, s, processed, entry, leave)
    return entry, leave


def dfs(edges, s, processed, entry, leave):
    time = 0
    stack = [s]
    while len(stack) > 0:
        v = stack.pop()
        if processed[v] is None:
            entry[v] = time
            processed[v] = False
            stack.append(v)
            time += 1
            for w in sorted(edges[v], reverse=True):
                if processed[w] is None:
                    stack.append(w)
        elif processed[v] is False:
            leave[v] = time
            processed[v] = True
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
    entry, leave = main_dfs(edges, 1)
    for i in range(1, n + 1):
        print(entry[i], leave[i])
