class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        binary_codes = set()
        idx = 0
        while idx <= len(s) - k:
            binary_codes.add(s[idx:idx+k])
            idx += 1
            
        return len(binary_codes) == 2 ** k