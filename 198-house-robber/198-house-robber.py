class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return(nums[0])
        
        dp[1] = nums[0]
        
        for idx in range(2, len(nums) + 1):
            dp[idx] = max(nums[idx-1] + dp[idx-2], dp[idx-1])
        
        return dp[len(nums)]