from collections import defaultdict


def dfs(edges, s, entry, leave):
    time = 0
    is_black = [None] * (n + 1)
    stack = [s]
    while len(stack) > 0:
        s = stack.pop()
        if is_black[s] is None:
            entry[s] = time
            is_black[s] = False
            stack.append(s)
            time += 1
            for w in edges[s]:
                if is_black[w] is None:
                    stack.append(w)
        elif is_black[s] is False:
            leave[s] = time
            is_black[s] = True
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
    entry = [None] * (n + 1)
    leave = [None] * (n + 1)
    dfs(edges, 1, entry, leave)
    for i in range(1, n + 1):
        print(entry[i], leave[i])
