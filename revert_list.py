def solution(node):
    while node:
        next_node = node.next
        node.next = node.prev
        node.prev = next_node
        if next_node is None:
            break
        node = next_node
    return node
