from collections import Counter


def magic_words():
    t = input()
    s = input()
    len_s = len(s)
    t_lis = list(t)
    s_counter = Counter(s)
    t_counter = Counter(t_lis[:len_s])
    statistic = dict()
    summ = 0
    for e in s_counter:
        statistic[e] = [s_counter[e], min(s_counter[e], t_counter[e])]
        summ += statistic[e][1]
    for i in range(len(t) - len(s) + 1):
        if summ == len_s - 1:
            print(i)
            break
        if t[i] in statistic:
            if statistic[t[i]][1] > 0:
                statistic[t[i]][1] -= 1
                summ -= 1
        if i + len_s < len(t) and t[i + len_s] in statistic:
            if statistic[t[i + len_s]][1] < statistic[t[i + len_s]][0]:
                statistic[t[i + len_s]][1] += 1
                summ += 1
    else:
        print(-1)


if __name__ == '__main__':
    magic_words()