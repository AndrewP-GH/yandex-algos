# Отчет: https://contest.yandex.ru/contest/25070/run-report/68701938/
#
# Алгоритм работы:
# Считаем, что в случае дороги 'R', мы имеем спрямую свзять м/у городами (N) -> (N+M),
#   а в случае 'B' - обратно (N+M) -> (N).
# Тогда задача сводится к задаче поиска циклов в графе. Поскольку по условию задачи карта считается оптимальной, если
#   существует путь из A в B только по одному типу дорог, перевернув направление дороги для одного из типов (B), мы
#   получим задачу проверки графа на отсутсвие циклов, потому что если цикл имеется, значит существуют пути A -> B и
#   B -> A, т.е. мы можем попасть из A в B по двум типам дорог, и карта не является оптимальной.
# Для хранения вершин используем список смежности.
# Для поиска будем использовать модернизированный алгоритм поиска в глубину DFS:
#   если во время проверки соседних нод мы встречаем серую ноду (ту, которую уже добавли в план обхода), значит мы нашли
#   цикл и граф дорог не является оптимальным.
#
# Алгоритмическая сложность: n - количество вершин в графе, m - количество ребер в графе.
# - суммарная вставка в словарь: O(m)
# - суммарная сложность алгоритма проверки на оптимальность графа: O(n + m), т.к. алгоритм должен проверить все вершины,
#   ему придется пройтись по всем спискам смежности.
# В итоге ассимптотическая сложность будет: O(n + m).
#
# Алгоритм требует лишь O(m) памяти для словаря с начальными данными, и O(n) для хранения информации о посещенных
#   вершинах.
# Итоговая: O(n + m).


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
