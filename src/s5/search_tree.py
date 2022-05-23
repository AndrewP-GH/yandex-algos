# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root) -> bool:
    return check_value(root, None, None)


def check_value(node, left, right):
    if node is None:
        return True

    if left and node.value <= left.value:
        return False

    if right is not None and node.value >= right.value:
        return False

    return check_value(node.left, left, node) \
           and check_value(node.right, node, right)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == "__main__":
    test()
