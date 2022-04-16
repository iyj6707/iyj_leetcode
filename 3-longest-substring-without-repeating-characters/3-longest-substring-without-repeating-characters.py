class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        substr = ""
        ans = 0
        while end < len(s):
            if s[end] not in substr:
                substr += s[end]
            else:
                ans = max(ans, len(substr))
                start = s[start:].index(s[end]) + 1 + start
                substr = ''.join(s[start:end + 1])
            end += 1
        return max(ans, len(substr))
                