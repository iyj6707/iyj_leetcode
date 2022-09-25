class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        
        if target == 0:
            return len(nums)
        
        curr_sum, max_len = 0, 0
        start_idx = 0
        
        for end_idx in range(len(nums)):
            curr_sum += nums[end_idx]
            while start_idx <= end_idx and curr_sum > target:
                curr_sum -= nums[start_idx]
                start_idx += 1
            if curr_sum == target:
                max_len = max(max_len, end_idx - start_idx + 1)
                
        return -1 if max_len == 0 else len(nums) - max_len