def main():
    n = int(input())
    i_2 = 1
    i_1 = 1
    if n in (0, 1):
        return 1
    for _ in range(n - 1):
        res = i_2 + i_1
        i_2 = i_1
        i_1 = res
    return i_1


if __name__ == '__main__':
    print(main())
