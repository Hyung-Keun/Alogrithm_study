def lengthOfLongestSubstring(s):
    d = {}
    res = start = 0

    for i, c in enumerate(s):
        if c in d and start <= d[c]:
            start = d[c] + 1
        else:
            res = max(res, i - start + 1)

        d[c] = i

    return res

print(lengthOfLongestSubstring("abcabcbb"))