class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        S = 0
        M = len(nums)
        for num in nums:
            S += num
        return M * (M + 1) // 2 - S
        