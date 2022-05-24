# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root) -> bool:
    return is_anagram(root)


def is_anagram(root) -> bool:
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is None or root.right is None:
        return False
    left_order = []
    traverse(root.left, left_order, True)
    right_order = []
    traverse(root.right, right_order, False)
    return left_order == right_order


def traverse(root, order_list, l_to_r):
    order_list.append(root.value if root else None)
    if root is None:
        return
    if l_to_r:
        traverse(root.left, order_list, l_to_r)
        traverse(root.right, order_list, l_to_r)
    else:
        traverse(root.right, order_list, l_to_r)
        traverse(root.left, order_list, l_to_r)


def test():
    node1 = Node(3, None, None)
    node2 = Node(4, None, None)
    node3 = Node(4, None, None)
    node4 = Node(3, None, None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)


if __name__ == '__main__':
    test()
