from collections import defaultdict


def adjacent_list(n, edges):
    linked_list = defaultdict(list)
    for edge in edges:
        linked_list[edge[0]].append(edge[1])
    for i in range(n):
        numb = i + 1
        if numb not in linked_list:
            print(0)
        else:
            sl = sorted(linked_list[numb])
            print(len(sl), end=" ")
            print(" ".join(map(str, sl)))


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
    adjacent_list(n, edges)
