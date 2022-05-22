class Solution:
    def countSubstrings(self, s: str) -> int:
        s_len = len(s)
        size = 1
        ans = 0
        
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        while size <= s_len + 1:
            for idx in range(s_len - size + 1):
                if is_palindrome(s[idx:idx+size]):
                    ans += 1
            size += 1
            
        return ans
        