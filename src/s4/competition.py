import sys


def competition():
    n = int(input())
    rounds = sys.stdin.readline().rstrip().split()
    max_len = 0
    curr_sum = 0
    hash_map = {}
    for i in range(n):
        if rounds[i] == '1':
            curr_sum += 1
        else:
            curr_sum -= 1
        if curr_sum == 0:
            max_len = i + 1
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:
            hash_map[curr_sum] = i
    return max_len


if __name__ == '__main__':
    res = competition()
    print(res)
