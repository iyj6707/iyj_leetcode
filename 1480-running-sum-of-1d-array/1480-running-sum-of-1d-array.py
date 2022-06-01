class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        S = 0
        ans = []
        for num in nums:
            S += num
            ans.append(S)
        return ans