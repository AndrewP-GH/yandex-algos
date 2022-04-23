# Отчет 67725389: https://contest.yandex.ru/contest/24414/run-report/67725389/
# Алгоритм работы:
# 1) Внутренний размер таблицы задается как большое простое число с википедии
# 2) Для устранения коллизий используется связный список (со вставкой в начало)
# Сложность операций в такой структуре данных O(1) (считаем коллизии, из-за которых приходится ходить по односвязному
#   списку и сравнивать между собой строки за O(n*m), где n - средняя длина строки (ключа), m - количество узлов в
#   односвязном списке, редкими.
# Сложность по памяти O(n) (по количеству элементов в таблице)
# Суммарное время работы: O(n), где n - кол-во операций (get, put, delete) с хеш-таблицей

class FixedHashTable(object):
    class Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity):
        self._capacity = capacity
        self._values = [None] * capacity

    def __hashing(self, key):
        return int(key) % self._capacity

    @staticmethod
    def __get_value(node):
        return (True, node.value) if node else (False, None)

    def put(self, key, value):
        key_hash = self.__hashing(key)
        head = self._values[key_hash]
        if head is None:
            self._values[key_hash] = self.Node(key, value)
            return
        node = head
        while node and node.key != key:
            node = node.next
        if node:
            node.value = value
        else:
            node = self.Node(key, value)
            self._values[key_hash] = node
            node.next = head

    def get(self, key):
        key_hash = self.__hashing(key)
        head = self._values[key_hash]
        node = head
        while node and node.key != key:
            node = node.next
        return self.__get_value(node)

    def delete(self, key):
        key_hash = self.__hashing(key)
        node = self._values[key_hash]
        prev = None
        while node and node.key != key:
            prev = node
            node = node.next
        if node:
            if prev:
                prev.next = node.next
            else:
                self._values[key_hash] = node.next
        return self.__get_value(node)


def simple_hash_table():
    ht = FixedHashTable(514229)
    n = int(input())
    for _ in range(n):
        command = input().split()
        try:
            result = getattr(ht, command[0])(*command[1:])
            if result:
                print(result[1])
        except ValueError:
            print('error')


if __name__ == '__main__':
    simple_hash_table()
