import sys


def common_subarray_efficient():
    n = int(input())
    first = sys.stdin.readline().rstrip().split()
    m = int(input())
    second = sys.stdin.readline().rstrip().split()
    hash_set = set()
    for i in range(n):
        for j in range(m):
            if first[i] == second[j]:
                hash_set.add((i, j))
    max_len, curr_len = 0, 0
    for t in hash_set:
        if max_len > len(hash_set) / 2:
            return max_len
        curr_len = 1
        i, j = t
        while (i + 1, j + 1) in hash_set:
            curr_len += 1
            i += 1
            j += 1
        max_len = max(max_len, curr_len)
    return max_len


if __name__ == '__main__':
    res = common_subarray_efficient()
    print(res)
