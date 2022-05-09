class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_letter = {
            "2": ["a", "b", "c"], 
            "3": ["d", "e", "f"], 
            "4": ["g", "h", "i"], 
            "5": ["j", "k", "l"], 
            "6": ["m", "n", "o"], 
            "7": ["p", "q", "r", "s"], 
            "8": ["t", "u", "v"], 
            "9": ["w", "x", "y", "z"]
        }
        
        permute = []
        for digit in digits:
            permute.append(phone_letter[digit])
        
        ans = []
        def dfs(start, ans_str, depth):
            if depth == len(digits):
                ans.append(ans_str)
                return
            
            for j in range(len(permute[depth])):
                dfs(start + 1, ans_str + permute[depth][j], depth + 1)

        dfs(0, "", 0)
                    
        return ans
                
            
            
            
    