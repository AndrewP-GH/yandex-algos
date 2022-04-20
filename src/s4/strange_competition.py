def strange_competition():
    first = input().rstrip()
    second = input().rstrip()
    if len(first) != len(second):
        return "NO"
    f_to_s = {}
    s_to_f = {}
    for i in range(len(first)):
        f = first[i]
        s = second[i]
        if f in f_to_s:
            if f_to_s[f] != s:
                return "NO"
        else:
            f_to_s[f] = s
        if s in s_to_f:
            if s_to_f[s] != f:
                return "NO"
        else:
            s_to_f[s] = f
    return "YES"


if __name__ == "__main__":
    res = strange_competition()
    print(res)
