def merge(arr: list, lf: int, mid: int, rg: int) -> list:
    left, right = arr[lf:mid], arr[mid:rg]
    result = [None] * (rg - lf)
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1
    while l < len(left):
        result[k] = left[l]
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]
        r += 1
        k += 1
    return result


def merge_sort(arr: list, lf: int, rg: int) -> None:
    if rg - lf == 1:
        return
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    arr[lf:rg] = merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
