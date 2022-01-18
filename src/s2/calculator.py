import sys


class Node:
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev


class Stack:
    def __init__(self):
        self._head = None,
        self._size = 0

    def push(self, value):
        node = Node(value, self._head)
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
