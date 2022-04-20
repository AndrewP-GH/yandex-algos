def substrings():
    string = input().rstrip()
    hash_map = {}
    max_len = 0
    curr_len = 0
    start_pos = 0
    str_len = len(string)
    for i in range(str_len):
        c = string[i]
        curr_len += 1
        if c in hash_map:
            prev_index = hash_map[c]
            if prev_index >= start_pos:
                curr_len -= hash_map[c] + 1
                start_pos = hash_map[c] + 1
        hash_map[c] = i
        max_len = max(max_len, curr_len)
    return max_len


if __name__ == '__main__':
    res = substrings()
    print(res)
