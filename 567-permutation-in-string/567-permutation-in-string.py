class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def makeHashTable(s: str):
            hash_table = defaultdict(int)
            for ch in s:
                hash_table[ch] += 1
            return hash_table
            
        start = 0
        end = len(s1)
        s1_dict = makeHashTable(s1)
        
        if len(s1) > len(s2):
            return False
        
        while end <= len(s2):
            if s1_dict == makeHashTable(s2[start:end]):
                return True
            start += 1
            end += 1
        return False