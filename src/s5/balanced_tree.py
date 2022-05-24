# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root) -> bool:
    return is_balanced_by_height(root)[1]


def is_balanced_by_height(root, is_balanced=True):
    if root is None or not is_balanced:
        return 0, is_balanced
    l_height, is_balanced = is_balanced_by_height(root.left, is_balanced)
    r_height, is_balanced = is_balanced_by_height(root.right, is_balanced)
    if abs(l_height - r_height) > 1:
        is_balanced = False

    return max(l_height, r_height) + 1, is_balanced


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == "__main__":
    test()
