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
        
        ans = []
        def dfs(ans_str, depth):
            if depth == len(digits):
                ans.append(ans_str)
                return
            
            for letter in phone_letter[digits[depth]]:
                dfs(ans_str + letter, depth + 1)

        dfs("", 0)
                    
        return ans
                
            
            
            
    