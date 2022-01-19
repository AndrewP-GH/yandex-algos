# -- ПРИНЦИП РАБОТЫ --
# Я реализовал деку на кольцевом буфере
# Добавление в начало/конец и удаление из начала/конца происходит за O(1),
# поскольку у меня есть указатели на начало и конец массива
# Поскольку буффер кольцевой, все операции над указателями происходят по модулю длиный массива.
# Дека потребялет константый размер памяти O(n)
# Ошибки передаю в качестве возвращаемого значения (как объект или вторым параметром кортежа).
# Отчет 64130697 https://contest.yandex.ru/contest/22781/run-report/64130697/


class Deque:
    def __init__(self, n):
        self._max_size = n
        self._buffer = [None] * n
        self._size = 0
        self._head = 0
        self._tail = 0

    def push_back(self, value):
        if self._size == self._max_size:
            raise ValueError
        self._buffer[self._tail] = value
        self._tail = (self._tail + 1) % self._max_size
        self._size += 1

    def push_front(self, value):
        if self._size == self._max_size:
            raise ValueError
        # я знаю про обратную индексацию в питоне, но так алгоритмически правильнее
        self._head = (self._head - 1 + self._max_size) % self._max_size
        self._buffer[self._head] = value
        self._size += 1

    def pop_back(self):
        if self._size == 0:
            raise ValueError
        self._tail = (self._tail - 1 + self._max_size) % self._max_size
        value = self._buffer[self._tail]
        self._buffer[self._tail] = None
        self._size -= 1
        return value

    def pop_front(self):
        if self._size == 0:
            raise ValueError
        value = self._buffer[self._head]
        self._buffer[self._head] = None
        self._head = (self._head + 1) % self._max_size
        self._size -= 1
        return value


def main():
    n = int(input())
    m = int(input())
    deque = Deque(m)
    for _ in range(n):
        command = input().split()
        try:
            res = getattr(deque, command[0])(*command[1:])
            if res is not None:
                print(res)
        except ValueError:
            print('error')


if __name__ == '__main__':
    main()
