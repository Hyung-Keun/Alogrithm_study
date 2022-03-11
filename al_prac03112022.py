#Q.  다음과 같은 문자열을 입력받았을 때,
#어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오
#해결책 2개. 둘 중에 뭐가 나을까요?

import string
from pprint import pprint

text = 'hello, this is sparta'

counter = {}
# 21 번 연산 -> 길이만큼 연산 len(text)
#n번 일어난다 -> O(n)의 시간을 가진다
for char in text:
    if not char.isalpha():
        continue #이게 아니라면 건너가라
    if char in counter:
        counter[char] += 1
    else:
        counter[char] = 1
pprint(counter)
# pretty print 이쁘게 생산
counter2 = {}
# 26 * 21 번 연산 -> 알파벳 갯수 * text글자 연산
#n^2 일어난다 -> O(n^2)의 시간을 가진다.
for lo in string.ascii_lowercase: #a-z까지 다 알파벳순으로 쭉 나열했을때
    for char in text:
        if lo == char:
            if lo in counter2:
                counter2[lo] += 1
            else:
                counter2[lo] = 1
pprint(counter2)

# 전자의 코드가 더 효율적인 코드이다. 시간복잡도가 위에 것이 훨씬좋다.
#중첩 for문 -> 다시 체크해라 (꿀팁). 의도된 중첩된 for문은 별로없다.
#중첩 for문 너무 시간이 오래걸린다.

#배열에서 특정 요소 찾기
#다음과 같은 숫자로 이루어진 배열이 있을 때,
# 이 배열 내에 특정 숫자가 존재한다면 True, 존재하지 않다면 False 를 반환하시오.
#arr = [3, 5, 6, 1, 2, 4]; num = 10;
def is_number_exist(num, arr):
    for el in arr:
        if num == el:
            return True
    return False

#print(is_number_exist(num, arr))
#1.알고리즘을 만들때 생각: 입력값에 비례해서 얼마나 늘어날지 파악: 1? N? N^2?
#2.공간복잡도 보다는 시간복잡도를 더 줄이기 위해 고민하자.
#3.최악의 경우에 시간이 얼마나 소요될지(빅오표기법)에대해 고민하자.

#알파벳찾기문제
#알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
# 배열로 처리하는게 중요!
#답안
#O(N^2)
def get_idx_naive(word):
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        char = word[i]
        for j in range(len(string.ascii_lowercase)):
            lo = string.ascii_lowercase[j]
            if result[j] == -1 and char == lo:
                result[j] = i
    print(result)
    print(' '.join([str(num) for num in result])) #result를 기준으로 for 문을 돌릴건데 각 요소를 우선 문자로 만들어줘
    #그다음에 바뀐 애들을 합쳐. 그런데, 요소와 요소 사이마다 ' ' 공백을 좀 줘바.


def get_idx(word):
    # point 1. ord
    # point 2. O(n^2) -> O(n)
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        idx = ord(word[i]) - 97
        #ord -> 문자를 숫자로 바꿔주는것. 알파벱 대소문자를 숫자로 바꿔주는 아이.
        #아스키 코드대로 해준다.
        if result[idx] == -1:
            result[idx] = i
    print(' '.join([str(num) for num in result]))


get_idx_naive('baekjoon')
get_idx('baekjoon')