class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(x, y):
            if (
                not (0 <= x <= len(grid) - 1)
                or not (0 <= y <= len(grid[0]) - 1)
                or grid[x][y] == 0
                or (x, y) in visited
            ):
                return 0

            visited.add((x, y))
            sum = 0
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                sum = max(sum, dfs(nx, ny))
            
            visited.remove((x, y)) 
            return sum + grid[x][y]

        res = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                visited = set()
                res = max(res, dfs(i, j))
        return res

