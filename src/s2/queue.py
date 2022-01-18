import sys


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Queue:
    def __init__(self):
        self._head = None
        self._size = 0
        self._tail = None

    def get(self):
        if self._size == 0:
            return 'error'
        res = self._head.value
        self._head = self._head.next
        self._size -= 1
        return res

    def put(self, value):
        node = Node(value)
        if self._size == 0:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def size(self):
        return self._size


def main():
    queue = Queue()
    n = int(input())
    for _ in range(n):
        command = sys.stdin.readline().rstrip().split()
        if command[0] == 'put':
            queue.put(command[1])
        elif command[0] == 'get':
            print(queue.get())
        elif command[0] == 'size':
            print(queue.size())


if __name__ == '__main__':
    main()
