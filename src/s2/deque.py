# -- ПРИНЦИП РАБОТЫ --
# Я реализовал деку на кольцевом буфере
# Добавление в начало/конец и удаление из начала/конца происходит за O(1),
# поскольку у меня есть указатели на начало и конец массива
# Поскольку буффер кольцевой, все операции над указателями происходят по модулю длиный массива.
# Дека потребялет константый размер памяти O(n)
# Ошибки передаю в качестве возвращаемого значения (как объект или вторым параметром кортежа).
# Отчет 64074207 https://contest.yandex.ru/contest/22781/run-report/64074207/


class Deque:
    def __init__(self, n):
        self._max_size = n
        self._buffer = [None] * n
        self._size = 0
        self._head = 0
        self._tail = 0

    def push_back(self, value):
        if self._size == self._max_size:
            return 'error'
        self._buffer[self._tail] = value
        self._tail = (self._tail + 1) % self._max_size
        self._size += 1
        return None

    def push_front(self, value):
        if self._size == self._max_size:
            return 'error'
        # я знаю про обратную индексацию в питоне, но так алгоритмически правильнее
        self._head = (self._head - 1 + self._max_size) % self._max_size
        self._buffer[self._head] = value
        self._size += 1
        return None

    def pop_back(self):
        if self._size == 0:
            return None, 'error'
        self._tail = (self._tail - 1 + self._max_size) % self._max_size
        value = self._buffer[self._tail]
        self._buffer[self._tail] = None
        self._size -= 1
        return value, None

    def pop_front(self):
        if self._size == 0:
            return None, 'error'
        value = self._buffer[self._head]
        self._buffer[self._head] = None
        self._head = (self._head + 1) % self._max_size
        self._size -= 1
        return value, None


def main():
    n = int(input())
    m = int(input())
    deque = Deque(m)
    for _ in range(n):
        command = input().split()
        if command[0] == 'push_back':
            err = deque.push_back(command[1])
            if err is not None:
                print(err)
        elif command[0] == 'push_front':
            err = deque.push_front(command[1])
            if err is not None:
                print(err)
        elif command[0] == 'pop_front':
            res, err = deque.pop_front()
            print(res if res is not None else err)
        elif command[0] == 'pop_back':
            res, err = deque.pop_back()
            print(res if res is not None else err)


if __name__ == '__main__':
    main()
