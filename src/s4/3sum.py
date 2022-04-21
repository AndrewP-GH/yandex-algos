def _3sum_o_1(nums, A):
    nums.sort()
    size = len(nums)
    result = set()
    for i in range(size - 2):
        l = i + 1
        r = size - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == A:
                result.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
            elif s < A:
                l += 1
            else:
                r -= 1
    return result


def _3sum_o_n(nums, A):
    size = len(nums)
    result = set()
    history = set()
    for i in range(size - 1):
        for j in range(i + 1, size):
            s = nums[i] + nums[j]
            diff = A - s
            if diff in history:
                result.add((diff, nums[i], nums[j]))
        history.add(nums[i])
    return result


if __name__ == '__main__':
    nums = [5, 2, 8, 1, 1, 3, 4, 4]
    A = 10
    print(_3sum_o_1(nums, A))
    print(_3sum_o_n(nums, A))
