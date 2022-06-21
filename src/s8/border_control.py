import unittest


def border_control(first: str, second: str) -> str:
    return "OK" if compare_strings(first, second) else "FAIL"


def compare_strings(first: str, second: str) -> bool:
    if abs(len(first) - len(second)) > 1:
        return False
    make_change = False
    min_len = min(len(first), len(second))
    i, j = 0, 0
    for _ in range(min_len):
        if first[i] != second[j]:
            if make_change:
                return False
            else:
                make_change = True
                if len(first) > len(second):
                    j -= 1
                elif len(first) < len(second):
                    i -= 1
        i += 1
        j += 1
    return True


if __name__ == '__main__':
    _first = input()
    _second = input()
    print(border_control(_first, _second))


class TestBorderControl(unittest.TestCase):
    def test_first(self):
        self.assertEqual(border_control('abcdefg', 'abdefg'), 'OK')

    def test_second(self):
        self.assertEqual(border_control('helo', 'hello'), 'OK')

    def test_third(self):
        self.assertEqual(border_control('dog', 'fog'), 'OK')
