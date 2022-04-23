# Отчет 67707529: https://contest.yandex.ru/contest/24414/run-report/67707529/
# Алгоритм работы:
# 1) Собрать статистику по всем словам из документов, для этого мы создаем словарь, у которого ключем будет слово,
#   а значение - другой словарь, с ключем в виде номера документа и значением равным числу вхождений этого слова
#   в данный документ.
#   Алгоритмическая сложность O(n*m), т.к. поиск и вставка слова осуществляются за O(1), где n - количество документов,
#   а m - количество слов в каждом документе, размер слов при этом влият лишь на сложность устранения коллизий,
#   которые считаю редкими.
#   Сложность по памяти - O(m), m - количество уникальных слов.
# 2) Для каждой строки поиска надо
#   а) оставить только уникальные слова
#   б) посчитать сколько каждое слово встречается в каждом документе
#   в) отсортировать полученый результат по кол-ву совпадений, и номеру документа, затем взять 5 наиболее релевантных
#   Алгоритмическая сложность поиска и подсчета будет O(l), где l - количество уникальных слов в запросе,
#   этап 2 будет выполняться k раз (по кол-ву запросов), поэтому итоговая сложность будет O(k(l + n*log(n))),
#   где n - число документов, в которых встречаются слова, это слагаемое возникает из-за необходимости сортировать
#   найденные документы, а в реальных запросах их может быть много.
#   Сложность по памяти - O(l), l - количество уникальных слов, но это сложность на каждом шаге (для каждого поиска),
#   и после обработки запроса память можно переиспользовать.
# 3) Вывести на экран результат поиска.
#   Итоговая алгоритмическая сложность O(n*m + k(l + n*log(n))), т.к. все вычисления происходят за O(1),
#   а число документов, слов и запросов неизвестно.
# Сложность по памяти - O(m + l), m - количество уникальных слов в документах, l - среднее количество уникальны слов
# в запросе.
# С Counter не укладываюсь в time limits :(

import sys
from collections import defaultdict


def search_engine():
    statistics = init_statistics()
    m = int(input())
    for i in range(m):
        search_line = sys.stdin.readline().rstrip().split()
        result = find_most_relevant(search_line, statistics, 5)
        print(*map(str, [x[0] for x in result]))


def init_statistics():
    n = int(input())
    statistics = defaultdict(lambda: defaultdict(int))
    for i in range(n):
        line = sys.stdin.readline().rstrip().split()
        doc_number = i + 1
        for word in line:
            statistics[word][doc_number] = statistics[word][doc_number] + 1
    return statistics


def find_most_relevant(search_line, statistics, n):
    unique_words = set(search_line)
    line_stat = defaultdict(int)
    for word in unique_words:
        doc_stat = statistics[word]
        for doc in doc_stat:
            line_stat[doc] += doc_stat[doc]
    result = sorted(line_stat.items(), key=lambda x: (-x[1], x[0]))[:n]  # sort by value desc, then by id asc
    return result


if __name__ == '__main__':
    search_engine()
