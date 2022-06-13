class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        row_num = len(triangle)
        
        for i in range(row_num):
            if i == 0:
                continue
            length = len(triangle[-i-1])
            for j in range(length):
                triangle[-i-1][j] += min(triangle[-i][j], triangle[-i][j+1])
            
        return triangle[0][0]
            