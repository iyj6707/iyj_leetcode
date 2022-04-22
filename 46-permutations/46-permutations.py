class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        ans = []
        cur = []
        
        def dfs(start):
            if len(cur) == length:
                ans.append(cur[:])
                return
            
            for i in range(start, length):
                if nums[i] in cur:
                    continue
                cur.append(nums[i])
                dfs(0)
                cur.pop()
        
        dfs(0)
        return ans