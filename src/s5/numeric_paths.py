# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root) -> int:
    return go(root, 0)


def go(node, root_value) -> int:
    if node is None:
        return 0
    new_value = root_value * 10 + node.value
    if node.left is None and node.right is None:
        return new_value
    return go(node.left, new_value) + go(node.right, new_value)


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    assert solution(node5) == 275


def test2():
    node1 = Node(1, None, None)
    node2 = Node(0, node1, None)

    assert solution(node2) == 1


if __name__ == "__main__":
    test()
