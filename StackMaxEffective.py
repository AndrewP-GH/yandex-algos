class Node:
    def __init__(self, value, prev=None, is_max=False):
        self.value = value
        self.prev = prev
        self.is_max = is_max


class StackMax:
    def __init__(self):
        self.maximum = []
        self.head = None

    def push(self, value):
        is_max = False
        if self.head is None or self.maximum[-1] <= value:
            is_max = True
            self.maximum.append(value)
        node = Node(value, self.head, is_max)
        self.head = node

    def pop(self):
        if self.head is None:
            return None, 'error'
        node = self.head
        self.head = self.head.prev
        if node.is_max:
            del self.maximum[-1]
        return node.value, None

    def get_max(self):
        if self.head is None:
            return None, 'None'
        return self.maximum[-1], None


def main():
    stack = StackMax()
    n = int(input())
    for i in range(n):
        command = input().split()
        if command[0] == 'get_max':
            res = stack.get_max()
            print(res[0] if res[0] is not None else res[1])
        elif command[0] == 'push':
            stack.push(int(command[1]))
        elif command[0] == 'pop':
            res = stack.pop()
            if res[1] is not None:
                print(res[1])


if __name__ == '__main__':
    main()
