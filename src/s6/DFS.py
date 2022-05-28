from collections import defaultdict


def main_dfs(edges, s):
    processed = [None] * (n + 1)
    return dfs(edges, s, processed)


def print_res(res):
    print(" ".join(map(str, res)), end=" ")


def dfs(edges, s, processed):
    result = []
    stack = [s]
    while len(stack) > 0:
        v = stack.pop()
        if processed[v] is None:
            processed[v] = False
            stack.append(v)
            result.append(v)
            for w in sorted(edges[v], reverse=True):
                if processed[w] is None:
                    stack.append(w)
        elif processed[v] is False:
            processed[v] = True
    return result


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
        edges[v].append(u)
    s = int(input())
    result = main_dfs(edges, s)
    print(' '.join(map(str, result)))
