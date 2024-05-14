class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        for row in grid: 
            if row[0] == 0: 
                for i in range(len(row)): 
                    row[i] = row[i] ^ 1
        
        for j in range(len(grid[0])): 
            count = 0
            for i in range(len(grid)): 
                count += grid[i][j]
            if count <= len(grid) // 2: 
                for i in range(len(grid)):
                    grid[i][j] = grid[i][j] ^ 1
               
        
        ans = 0 
        for row in grid: 
            ans += int(''.join(str(x) for x in row), 2)
        
        return ans
