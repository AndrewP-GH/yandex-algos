import sys


def main():
    letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    number = sys.stdin.readline().rstrip()
    generate(0, number, len(number), '', letters)


def generate(current_len, number, number_len, result, letters):
    if current_len == number_len:
        return print(result, end=' ')
    line = letters[number[current_len]]
    for i in line:
        generate(current_len + 1, number, number_len, result + i, letters)


if __name__ == '__main__':
    main()
