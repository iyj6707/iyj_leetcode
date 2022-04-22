class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        length = len(s)
        cur = []
        ans = []
        
        def dfs(start):
            if len(cur) == length:
                ans.append(''.join(cur[:]))
                return
            
            for i in range(start, length):
                if s[i].isalpha():
                    if s[i].isupper():
                        cur.append(s[i].lower())
                        dfs(i + 1)
                        cur.pop()
                        cur.append(s[i].upper())
                        dfs(i + 1)
                        cur.pop()
                    else:
                        cur.append(s[i].upper())
                        dfs(i + 1)
                        cur.pop()
                        cur.append(s[i].lower())
                        dfs(i + 1)
                        cur.pop()
                else:
                    cur.append(s[i])
                    dfs(i + 1)
                    cur.pop()
                
        dfs(0)
        return ans
                    