def sift_down(heap, idx):
    left = idx * 2
    right = idx * 2 + 1
    if len(heap) <= left:  # нет дочерних узлов
        return idx
    if right < len(heap) and heap[left] < heap[right]:
        largest = right
    else:
        largest = left
    if heap[idx] < heap[largest]:
        heap[idx], heap[largest] = heap[largest], heap[idx]
        return sift_down(heap, largest)
    return idx


def test():
    sample = [-1, 89, 69, 47]
    assert sift_down(sample, 2) == 2


if __name__ == "__main__":
    test()
