import sys


class MyQueueSized:
    def __init__(self, max_size):
        self._buffer = [None] * max_size
        self._head = 0
        self._tail = 0
        self._size = 0
        self._max_size = max_size

    def push(self, value):
        if self._size == self._max_size:
            return 'error'
        self._buffer[self._tail] = value
        self._tail = (self._tail + 1) % self._max_size
        self._size += 1
        return None

    def pop(self):
        if self._size == 0:
            return 'None'
        result = self._buffer[self._head]
        self._buffer[self._head] = None
        self._head = (self._head + 1) % self._max_size
        self._size -= 1
        return result

    def peek(self):
        if self._size == 0:
            return 'None'
        return self._buffer[self._head]

    def size(self):
        return self._size


def main():
    commands = int(input())
    queue_size = int(input())
    queue = MyQueueSized(queue_size)
    for _ in range(commands):
        command = sys.stdin.readline().rstrip().split()
        if command[0] == 'peek':
            print(queue.peek())
        elif command[0] == 'push':
            err = queue.push(command[1])
            if err is not None:
                print(err)
        elif command[0] == 'size':
            print(queue.size())
        elif command[0] == 'pop':
            print(queue.pop())


if __name__ == '__main__':
    main()
