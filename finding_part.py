import sys
import bisect
input = sys.stdin.readline

#Overall parts (N)
part_nums = int(input())
N = list(map(int, input().split()))
N.sort()
print(N)

#Checking parts (M)
check_nums = int(input())
M = list(map(int, input().split()))
M.sort()
print(M)

def binary_search_builtin(nums, target):
    idx = bisect.bisect_left(nums, target)
    if idx < len(nums) and nums[idx] == target:
        return idx
    else:
        return -1

for part in M:
    is_part_there = binary_search_builtin(N, part)
    if is_part_there != -1:
        print('Yeah  ')
    else:
        print('Nah  ')







'''
N = 5
[8, 3, 7, 9, 2]
M = 3
[5, 7, 9]
'''
