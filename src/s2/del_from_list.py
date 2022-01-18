def solution(node, index):
    if index == 0:
        return node.next_item
    tmp = node
    prev = node
    while index:
        prev = tmp
        tmp = tmp.next_item
        index -= 1
    prev.next_item = tmp.next_item
    return node
