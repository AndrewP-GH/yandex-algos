# -- ПРИНЦИП РАБОТЫ --
# Для того, чтобы собирать операнды использую стек
# Стек реализован с помощью односвязного списка
# Операции добавления/удаления элемента происходят за O(1),
# потому что все сводится к переприсваиванию указателя на вершину списка
# Сложность по памяти O(n), т.к. хранятся только узлы
# Вычислительная сложность тоже линейная O(n), т.к. я либо добавляю элементы на стек за O(1),
# либо достаю их оттуда (сразу 2) тоже за O(1)
# Доказательство: если предполагается n арифметических операций, то в среднем/худшем случае это будет:
# (2 вставки + 2 извлечения + 1 вставка (результат)) * n операций, т.е. O(n).
# Отчет 64072427 https://contest.yandex.ru/contest/22781/run-report/64072427/

import sys


class Stack:
    def __init__(self):
        self._head = None,
        self._size = 0

    class Node:
        def __init__(self, value, prev=None):
            self.value = value
            self.prev = prev

    def push(self, value):
        node = self.Node(value, self._head)
        self._head = node
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise ValueError('Stack is empty')
        node = self._head
        self._head = self._head.prev
        self._size -= 1
        return node.value

    def size(self):
        return self._size


def main():
    stack = Stack()
    line = sys.stdin.readline().rstrip().split()
    for ch in line:
        if ch not in ('+', '-', '*', '/'):
            stack.push(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            if ch == '+':
                res = a + b
            elif ch == '-':
                res = a - b
            elif ch == '*':
                res = a * b
            elif ch == '/':
                res = a // b
            stack.push(res)
    print(stack.pop())


if __name__ == '__main__':
    main()
