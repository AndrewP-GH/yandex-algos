def main():
    h = [2, 7, 6, 9, 7, 5, 7, 3, 5]
    n = len(h)
    left = [None] * n
    right = [None] * n
    left[0] = -1
    right[-1] = n
    stack = [0]
    for i in range(1, n):
        calculate(i, stack, h, left, -1)
    stack.clear()
    stack = [n - 1]
    for i in range(n - 2, -1, -1):
        calculate(i, stack, h, right, n)
    print(f'left: {left}')
    print(f'right: {right}')
    s = [None] * n
    for i in range(n):
        s[i] = h[i] * (right[i] - left[i] - 1)
    print(f'S: {s}')
    m = max(s)
    print(f'MAX: {[i for i, x in enumerate(s) if x == m]}')


def calculate(i, stack, h, arr, bound):
    top = stack[-1]
    if h[top] < h[i]:
        stack.append(i)
        arr[i] = top
    else:
        while len(stack) > 0 and h[stack[-1]] >= h[i]:
            stack.pop()
        arr[i] = stack[-1] if len(stack) > 0 else bound
        stack.append(i)


if __name__ == '__main__':
    main()
