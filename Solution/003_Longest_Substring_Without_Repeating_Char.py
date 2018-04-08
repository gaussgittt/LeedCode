class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        res = 0
        left = 0

        for i, ch in enumerate(s):
            if ch in d and d[ch] >= left:
                left = d[ch] + 1
            d[ch] = i
            res = max(res, i - left + 1)

        return res

#debug
s = Solution()
print s.lengthOfLongestSubstring('aaaaabcccd')






'''Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must 

be a substring, "pwke" is a subsequence and not a substring.
'''