'''
n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
입력: [1, 4, 3, 2]
출력: 4
'''
#오름차순형식
nums = [1, 4, 3, 2]
print(nums.sort()) #sort()는 none 무조건 리턴하고, 원래 리스트 영향 sorted() 는 값을 리턴한다 그리고 원래 리스탑 영향 안준다
def array_partition():
    sum = 0
    pair = []
    nums.sort()
    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum
#짝수형식
def array_partition2():
    sum = 0;
    nums.sort()
    for i, n in enumerate(nums): #
            if i % 2 == 0:
                sum += n
    return sum

#파이썬스러운방식이야
def array_partition3():
    return sum(sorted(nums)[::2])## start, stop, step -> 슬라이싱 구문.