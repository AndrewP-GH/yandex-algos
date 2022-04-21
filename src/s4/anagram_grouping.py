import sys
from collections import defaultdict


def anagram_grouping():
    n = int(input())
    strings = sys.stdin.readline().rstrip().split()
    anagrams = defaultdict(list)
    for i in range(n):
        s = ''.join(sorted(strings[i]))
        anagrams[s].append(i)
    for v in sorted(anagrams.values()):
        print(' '.join(map(str, v)))


if __name__ == '__main__':
    anagram_grouping()
