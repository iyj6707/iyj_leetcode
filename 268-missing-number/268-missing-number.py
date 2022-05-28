class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        S = 0
        M = len(nums)
        return M * (M + 1) // 2 - sum(nums)
        