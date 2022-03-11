#역순
# word = "eever"
# def isPalindrome(word):
#     reversed_word = ' '
#     for a in word:
#         reversed_word = a + reversed_word
#     return reversed_word
# print(isPalindrome(word))


#Q. 알파벳 소문자로만 이루어진 문자열 S가 주어졌을 때, S의 부분 문자열 중에서 팰린드롬 이면서 길이가 가장 긴 것의 길이를 구하는 프로그램을 작성하시오.
'''
ex)
*입력    *출력
abab -> 3
banana -> 5
baekjoon -> 2
online -> 1
eevee -> 5
투포인터 사용?
'''
#팔린드롬
def longest_Palindrom(ssiba):
    for num in range(len(ssiba),0,-1):
        for num2 in range(len(ssiba)-num+1):
            if ssiba[num2:num2+num] == ssiba[num2:num2+num][::-1]:
                return num

# print(longest_Palindrom("씨알고리고알씨"))
