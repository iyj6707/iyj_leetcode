class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums_length = len(nums)
        ans = []
        
        def dfs(cur_list: List[int], depth: int, visited: List[int]):
            if depth == nums_length:
                if cur_list not in ans:
                    ans.append(cur_list[:])
                    return
            
            for idx in range(0, nums_length):
                if idx not in visited:
                    cur_list.append(nums[idx])
                    visited.append(idx)
                    dfs(cur_list, depth + 1, visited)
                    cur_list.pop()
                    visited.pop()
        
        dfs([], 0, [])
        
        return ans