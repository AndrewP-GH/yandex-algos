def substrings():
    string = input().rstrip()
    hash_map = {}
    max_len = 0
    start_pos = 0
    str_len = len(string)
    for i in range(str_len):
        c = string[i]
        if c in hash_map:
            start_pos = max(start_pos, hash_map[c] + 1)
        max_len = max(max_len, i - start_pos + 1)
        hash_map[c] = i
    return max_len


if __name__ == '__main__':
    res = substrings()
    print(res)
