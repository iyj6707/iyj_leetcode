class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        num_length = len(nums)
        
        right_ptr = 0
        big = nums[0]
        for i in range(num_length):
            if nums[i] < big:
                right_ptr = i
            else:
                big = nums[i]
        
        left_ptr = num_length - 1
        small = nums[-1]
        for i in range(num_length - 1, -1, -1):
            if nums[i] > small:
                left_ptr = i
            else:
                small = nums[i]
        
        return right_ptr - left_ptr + 1 if right_ptr != 0 else 0