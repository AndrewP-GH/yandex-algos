# Отчет: https://contest.yandex.ru/contest/25070/run-report/68682843/
#
# Алгоритм работы:
# 1. Создаем граф из всех вершин и всех ребер из входных данных. Для его хранения используется словарь
#   вида {u: [(v, w)]}, где w - вес ребра (u, v). Для простоты поиска, ребро добавляется дважды как кортеж (u, v) и (v, y)
# 2. Изначально считаем все вершины графа непосещенными
# 3. Берем первую попавшуюся вершину из графа
# 4. Удаляем ее из непосещенных и добавляем идущие из нее ребра в max-кучу (как критерий для сравнения используем вес
#   ребра), если вершина на другом конце еще не посещалась
# 5. В цикле, пока есть ребра в куче, и пока есть непосещенные вершины, берем ребро из кучи, и, если вершина на его
#   конце еще не посещалаяь, добавляем ее в остовное дерево и применяем к ней пункт 4. Если вершина посещалась, то
#   просто игнорируем это ребро.
# 6. Если после выполнения пункта 5 остались непосещенные вершины, это значит, что остовного дерево не существует,
#   иначе - возвращаем остовное дерево.
#
# Алгоритмическая сложность: n - количество вершин в графе, m - количество ребер в графе.
# - суммарная вставка в словарь: O(m)
# - суммарный проход по словарю и вставка ключей в set: O(m)
# - суммарное удаление вершины из посещенных и проверка, что ребро соединяет с непосещенной: O(n + m)
# - суммарные вставки в бинарную кучу: O(m*log(n))
# - просуммировать веса ребер остового дерева: O(m)
# В итоге ассимптотическая сложность будет: O(n + m + m*log(n)) = O(m*log(n))
#
# Алгоритм требует O(2*m) памяти для словаря с начальными данными, O(n) памяти для непосещенных вершин, O(m) памяти для
#   кучи и O(m) памяти для остового дерева.
# Итоговая - O(n+m).


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
    n, m = map(int, line)
    graph = defaultdict(list)
    for _ in range(m):
        line = stdin.readline().split()
        u, v, w = map(int, line)
        graph[u].append((v, w))
        graph[v].append((u, w))
    return n, m, graph


def add_vertex(v: int, graph: dict, not_added: set, edges: [MaxHeapObj]):
    not_added.remove(v)
    for u, w in graph[v]:
        if u in not_added:
            heapq.heappush(edges, MaxHeapObj(start=v, end=u, weight=w))


def find_mst_weight(n, m, graph) -> None | int:
    minimum_spanning_tree_weight = 0
    if m == 0:
        if n == 1:  # one node graph
            return minimum_spanning_tree_weight
        else:
            return None
    not_added = set(graph.keys())
    edges_max_heap = []

    v = list(graph.keys())[0]
    add_vertex(v, graph, not_added, edges_max_heap)
    while len(not_added) > 0 and len(edges_max_heap) > 0:
        edge = extract_maximum(edges_max_heap)
        if edge.end in not_added:
            add_vertex(edge.end, graph, not_added, edges_max_heap)
            minimum_spanning_tree_weight += edge.weight
    if len(not_added) > 0:
        return None
    else:
        return minimum_spanning_tree_weight


def extract_maximum(edges: [MaxHeapObj]):
    return heapq.heappop(edges)


def max_sum(n, m, graph):
    result = find_mst_weight(n, m, graph)
    if result is None:
        print("Oops! I did it again")
    else:
        print(result)


if __name__ == '__main__':
    _n, _m, _graph = init()
    max_sum(_n, _m, _graph)
