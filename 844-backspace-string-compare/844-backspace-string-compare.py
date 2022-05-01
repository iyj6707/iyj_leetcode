class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return True if self.operate(t) == self.operate(s) else False
    
    def operate(self, s: str) -> str:
        a = []
        for ch in s:
            if ch == "#":
                if a:
                    a.pop()
            else:
                a.append(ch)
        return ''.join(a)