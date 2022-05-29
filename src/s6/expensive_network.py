from __future__ import annotations

from sys import stdin
from collections import defaultdict
import heapq


class MaxHeapObj(object):
    def __init__(self, start: int, end: int, weight: int):
        self.start = start
        self.end = end
        self.weight = weight

    def __lt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight


def init():
    line = stdin.readline().split()
    n = int(line[0])
    m = int(line[1])
    graph = defaultdict(list)
    for _ in range(m):
        line = stdin.readline().split()
        u, v, w = int(line[0]), int(line[1]), int(line[2])
        graph[u].append((v, w))
        graph[v].append((u, w))
    return n, m, graph


def add_vertex(v: int, graph: dict, not_added: set, edges: [MaxHeapObj]):
    not_added.remove(v)
    for u, w in graph[v]:
        if u in not_added:
            heapq.heappush(edges, MaxHeapObj(start=v, end=u, weight=w))


def find_mst(n, m, graph) -> None | int | dict[tuple[int, int]: int]:
    if m == 0:
        if n == 1:  # one node graph
            return 1
        else:
            return None
    not_added = set(graph.keys())
    minimum_spanning_tree = {}
    edges_max_heap = []

    v = list(graph.keys())[0]
    add_vertex(v, graph, not_added, edges_max_heap)
    while len(not_added) > 0 and len(edges_max_heap) > 0:
        edge = extract_maximum(edges_max_heap)
        if edge.end in not_added:
            add_vertex(edge.end, graph, not_added, edges_max_heap)
            minimum_spanning_tree[(edge.start, edge.end)] = edge.weight
    if len(not_added) > 0:
        return None
    else:
        return minimum_spanning_tree


def extract_maximum(edges: [MaxHeapObj]):
    return heapq.heappop(edges)


def max_sum(n, m, graph):
    result = find_mst(n, m, graph)
    if result is None:
        print("Oops! I did it again")
    elif result == 1:
        print(0)
    else:
        print(sum(result.values()))


if __name__ == '__main__':
    _n, _m, _graph = init()
    max_sum(_n, _m, _graph)
