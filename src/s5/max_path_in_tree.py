# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class Store:
    def __init__(self):
        self.max_path = float('-inf')


# only root
# root + left
# root + right
# root + left + left
def solution(root) -> int:
    store = Store()
    find_max_path(root, store)
    return store.max_path


def find_max_path(root, store):
    if root is None:
        return 0
    left = find_max_path(root.left, store)
    right = find_max_path(root.right, store)
    max_subtree = max(left, right) + root.value
    max_tree = max(max_subtree, root.value)
    max_local_path = max(max_tree, left + right + root.value)
    store.max_path = max(store.max_path, max_local_path)
    return max_tree


def test():
    node1 = Node(5, None, None)
    node2 = Node(1, None, None)
    node3 = Node(-3, node2, node1)
    node4 = Node(2, None, None)
    node5 = Node(2, node4, node3)
    assert solution(node5) == 6


if __name__ == '__main__':
    test()

