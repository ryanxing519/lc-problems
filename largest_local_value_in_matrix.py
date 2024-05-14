class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        ans_grid = [[0] * (len(grid[0]) - 2) for _ in range(len(grid[0]) - 2)]

        for i in range(len(grid[0]) - 2):
            for j in range(len(grid[0]) - 2):

                ans = grid[i][j]

                for k in range(3):
                    for l in range(3):
                        ans = max(grid[i + k][j + l], ans)

                ans_grid[i][j] = ans

        return ans_grid
