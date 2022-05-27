from collections import defaultdict


def adjacency_matrix(n, edges):
    linked_list = defaultdict(set)
    for edge in edges:
        linked_list[edge[0]].add(edge[1])
    const = " ".join(map(str, [0] * n))
    for i in range(1, n + 1):
        if i in linked_list:
            line_set = linked_list[i]
            line = [1 if j in line_set else '0' for j in range(1, n + 1)]
            print(" ".join(map(str, line)))
        else:
            print(const)


if __name__ == '__main__':
    line = input().split()
    n = int(line[0])
    m = int(line[1])
    edges = []
    for _ in range(m):
        line = input().split()
        u = int(line[0])
        v = int(line[1])
        edges.append((u, v))
    adjacency_matrix(n, edges)
