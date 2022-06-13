import sys


def schedule(n, lessons):
    s_lessons = sorted(lessons, key=lambda x: (x[1], x[0]))
    result = [s_lessons[0]]
    for i in range(1, n):
        if s_lessons[i][0] >= result[-1][1]:
            result.append(s_lessons[i])
    return result


if __name__ == '__main__':
    _n = int(input())
    _lessons = [None] * _n
    for _i in range(_n):
        _start, _end = map(float, sys.stdin.readline().split())
        _lessons[_i] = (_start, _end)
    res = schedule(_n, _lessons)
    print(len(res))
    for r in res:
        print(r[0] if r[0] % 1 != 0 else int(r[0]), r[1] if r[1] % 1 != 0 else int(r[1]))
