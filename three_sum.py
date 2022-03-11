'''
Q. 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
입력.
nums = [-1, 0, 1, 2, -1, -4]
출력.
[
[-1, 0, 1],
[-1, -1, 2]
]
sort 쓰고, if문쓰고, 고정값쓴다음에 투포인터쓴다
lef, right
'''
nums = [-1, 0, 1, 2, -1, -4]
def threeSum(nums):
    result = []
    nums.sort() #nums = [-1, 0, 1, 2, -1, -4] -> [-4, -1, -1, 0, 1, 2]
    length = len(nums) #6
    for i in range(length - 2):
        if nums[i] > 0 or (i > 0 and nums[i] == nums[i - 1]):
            continue
        left, right = i + 1, length - 1
        while  left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                # 여기서 elif 가 아닌 if 로 처리하면 뒤의 esle 문과 맞물려 에러가 발생한다. else 가급적 쓰지말고 조건문을 추가해야될듯
                right -= 1
            else:
                result.append((nums[i], nums[left], nums[right]))
                print(result)

                while left < right and nums[left] == nums[left + 1]: #while문 살짝 if문이랑 for문 합친느낌
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))

