# Отчет https://contest.yandex.ru/contest/24810/run-report/68626848/
# Алгоритм работы:
# 1. Рекурсивно ищем узел с нужным ключом (т.к. алгоритм рекурсивный, мы на каждом шаге возвращаем корневой элемент
#   (под)дерева)
# 2. Если не нашли, не надо ничего делать
# 3. Если нашли, проверяем наличие правого и левого потомков
# 3.1 Если есть только левый потомок, переносим его вместо удаляемого
# 3.2 Если есть только правый потомок, переносим его вместо удаляемого
# 3.3 Если есть оба потомка, находим минимальный по ключу в правом поддереве и переносим его вместо удаляемого
# 3.3.1 Если у правого потомка нет левого поддерева, переносим его вместо удаляемого
# 3.3.2 Если у правого потомка есть левое поддерево, находим в нем самый левый лист и переносим его вместо удаляемого

# Т.к. мы обходим каждую вершину только 1 раз и на каждом шаге у нас "отбрасывается" одно из поддеревьев из поиска,
#  алгоритмическая сложность будет O(log(n)) в среднем и O(n) в худшем случае
# Т.к. алгоритм проводит операции над нодами и не использует дополнительных коллекций, сложность по памяти будет O(1).


# Comment it before submitting
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def remove(root, key) -> Node:
    if root is None:
        return root
    if root.value > key:
        root.left = remove(root.left, key)
        return root
    if root.value < key:
        root.right = remove(root.right, key)
        return root
    if root.left is None and root.right is None:
        return None
    if root.left is None:
        tmp = root.right
        root.right = None
        return tmp
    if root.right is None:
        tmp = root.left
        root.left = None
        return tmp
    # есть оба поддерева, находим минимальный элемент в правом поддереве
    prev = root
    new_root = root.right
    while new_root.left is not None:
        prev = new_root
        new_root = new_root.left
    if prev == root:
        new_root.left = prev.left
        return new_root
    prev.left = None
    new_root.left = root.left
    new_root.right = root.right
    return new_root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8


if __name__ == '__main__':
    test()
