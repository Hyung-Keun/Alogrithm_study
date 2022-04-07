import bisect
def binary_search_builtin(nums, target):
    idx = bisect.bisect_left(nums, target)
    # idx == len(nums) 가능하기 떄문.
    if idx < len(nums) and nums[idx] == target:
        return idx
    else:
        return -1


nums = [4, 5, 6, 7, 0, 1, 2] #0 1 2 4 5 6 7
target = 7
print(binary_search_builtin(sorted(nums), target))