def fibonacci_for_adults(n):
    m = (10 ** 9) + 7
    cache = [None] * (n + 1)
    cache[0] = 0
    cache[1] = 1
    for i in range(2, n + 1):
        cache[i] = (cache[i - 1] + cache[i - 2]) % m
    return cache[n]


if __name__ == '__main__':
    _n = int(input()) + 1
    print(fibonacci_for_adults(_n))
