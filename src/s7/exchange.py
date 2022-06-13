def exchange(n, values):
    if n <= 1:
        return 0
    gain = 0
    have_stock = False
    for i in range(n):
        current = values[i]
        next = values[i + 1] if (i + 1) < n else 0
        if next > current and not have_stock:
            have_stock = True
            gain -= current
        elif current > next and have_stock:
            have_stock = False
            gain += current
    return gain


if __name__ == '__main__':
    _n = int(input())
    _values = list(map(int, input().split()))
    print(exchange(_n, _values))

# 7 1 5 3 6 4       ->  7
# 1 2 3 4 5         ->  4
# 1 12 12 16 1 8    ->  22
