class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        cur = []
        ans = []
        
        def dfs(start):
            if len(cur) == k:
                ans.append(cur[:])
                return
            
            for num in range(start, n+1):
                cur.append(num)
                dfs(num + 1)
                cur.pop()
               
        dfs(1)
        
        return ans 
        