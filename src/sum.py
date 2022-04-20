def solve(numbers, target, result, number_index, combination):
    new_combination = combination.copy()
    new_combination.append(numbers[number_index])

    current_sum = sum(new_combination)
    if current_sum == target:
        result.append(new_combination.copy())
        return

    if number_index >= len(numbers) or current_sum > target:
        return

    solve(numbers, target, result, number_index + 1, new_combination)
    solve(numbers, target, result, number_index, new_combination)


def all_sum(bound, target):
    numbers = [0] * bound
    for i in range(bound):
        numbers[i] = i + 1

    result = []
    number_index = 0
    combination = []

    solve(numbers, target, result, number_index, combination)

    for s in result:
        for numb in s:
            print(numb, end=" ")
        print()


if __name__ == "__main__":
    k = int(input())
    n = int(input())
    all_sum(k, n)
