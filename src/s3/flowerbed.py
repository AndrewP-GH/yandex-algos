def flowerbad(n, array):
    array.sort(key=lambda x: (x[0], x[1]))
    result = []
    (left, right) = array[0]
    for i in range(1, n):
        (next_left, next_right) = array[i]
        if right >= next_left:
            right = max(right, next_right)
        else:
            result.append((left, right))
            left, right = next_left, next_right
    result.append((left, right))
    return result


if __name__ == '__main__':
    n = int(input())
    pieces = [None] * n
    for i in range(n):
        parts = input().rstrip().split()
        pieces[i] = (int(parts[0]), int(parts[1]))
    result = flowerbad(n, pieces)
    for tuple in result:
        print(tuple[0], tuple[1])
