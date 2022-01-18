import sys


def main():
    stack = []
    dictionary = {')': '(', ']': '[', '}': '{'}
    line = sys.stdin.readline().rstrip()
    for ch in line:
        if ch in dictionary:
            if len(stack) == 0 or dictionary[ch] != stack[-1]:
                return False
            else:
                del stack[-1]
        else:
            stack.append(ch)
    return len(stack) == 0


if __name__ == '__main__':
    print(main())
