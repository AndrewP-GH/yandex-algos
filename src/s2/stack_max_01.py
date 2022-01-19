class Stack:
    def __init__(self):
        self._top = None
        self._count = 0
        self._maximum = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

        def __str__(self):
            return "Node({})".format(self.value)

        __repr__ = __str__

    def __str__(self):
        temp = self._top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return 'Top {} \n\nStack :\n{}'.format(self._top, out)

    __repr__ = __str__

    def get_max(self):
        if self._top is None:
            return "Stack is empty"
        else:
            print("Maximum Element in the stack is: {}".format(self._maximum))

    def is_empty(self):
        if self._count == 0:
            return True
        else:
            return False

    def __len__(self):
        self._count = 0
        temp_node = self._top
        while temp_node:
            temp_node = temp_node.next
            self._count += 1
        return self._count

    def peek(self):
        if self._top is None:
            print("Stack is empty")
        else:
            if self._top.value > self._maximum:
                print("Top Most Element is: {}".format(self._maximum))
            else:
                print("Top Most Element is: {}".format(self._top.value))

    def push(self, value):
        if self._top is None:
            self._top = self.Node(value)
            self._maximum = value

        elif value > self._maximum:
            temp = (2 * value) - self._maximum
            new_node = self.Node(temp)
            new_node.next = self._top
            self._top = new_node
            self._maximum = value
        else:
            new_node = self.Node(value)
            new_node.next = self._top
            self._top = new_node
        print("Number Inserted: {}".format(value))

    def pop(self):
        if self._top is None:
            print("Stack is empty")
        else:
            removed_node = self._top.value
            self._top = self._top.next
            if removed_node > self._maximum:
                print("Top Most Element Removed :{} ".format(self._maximum))
                self._maximum = ((2 * self._maximum) - removed_node)
            else:
                print("Top Most Element Removed : {}".format(removed_node))


def main():
    stack = Stack()
    stack.push(3)
    stack.push(5)
    stack.get_max()
    stack.push(7)
    stack.push(19)
    stack.get_max()
    stack.pop()
    stack.get_max()
    stack.pop()
    stack.peek()


if __name__ == '__main__':
    main()
