#문자열 배열을 받아 애너그램 단위로 그룹핑하라.
'''
ex)
*입력
["eat", "tea", "tan", "ate", "nat", "bat"]
*출력
[
["ate", "eat", "tea"],
["nat", "tan"],
["bat"]
]
'''
# 내풀이생각: 첫번째, 각 문자들 단어 체크해서 같은 문자있는 단어끼리 묶어주기.
# 두번째, 묶은 단어끼리, 각 문자 바꿨을때 말이되는 단어되게 만들어주기

#정석풀이: 정렬하여 비교. sorted -> join -> append 정렬하고 합치고 붙여라.
#정렬: ['ate', 'bat', 'eat', 'nat', 'tan', 'tea'] sorted 사용시 print(sorted(example))
#합치고: atebateatnattantea join 사용시 print(''.join(sorted(example)))
#정답
#해쉬매핑 위주로 생각할것 이런문제들은
import collections

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
def group_anagram(strs):
    anagrams = collections.defaultdict(list)
    for word in strs:

        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())
print(group_anagram(strs))




