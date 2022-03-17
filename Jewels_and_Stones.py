'''
입력: J = "aA", S = "aAAbbbb"
출력: "3"
보석몇개있을까?
'''

def numJewelsIsInStones(J, S):
    freqs = {}
    count = 0
    #돌
    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1
    #보석
    for char in J:
        if char in freqs:
            count += freqs[char]
    return count
print(numJewelsIsInStones("aA", "aAAbbbb"))