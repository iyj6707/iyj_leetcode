class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        idx = 0
        
        while digits[-1 - idx] == 10:
            digits[-1 - idx] = 0
            if idx + 2 > len(digits):
                digits.insert(0, 1)
            else:
                digits[-2 - idx] += 1
            idx += 1
        
        return digits