class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        N, M = len(grid), len(grid[0])
        queue = []
        graph = [[float("inf")] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    graph[i][j] = 0

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (
                        (0 <= nx <= N - 1)
                        and (0 <= ny <= M - 1)
                        and graph[nx][ny] > graph[x][y] + 1
                    ):
                        queue.append((nx, ny))
                        graph[nx][ny] = graph[x][y] + 1

        def dfs(x, y, min_dist):

            if (
                not (0 <= x <= N - 1)
                or not (0 <= y <= M - 1)
                or graph[x][y] < min_dist
                or (x, y) in visited
            ):
                return False

            if x == N - 1 and y == M - 1:
                return True

            visited.add((x, y))

            return (
                dfs(x + 1, y, min_dist)
                or dfs(x - 1, y, min_dist)
                or dfs(x, y + 1, min_dist)
                or dfs(x, y - 1, min_dist)
            )

        l, r = 0, N + M
        ans = 0

        while l <= r:
            m = (l + r) // 2
            visited = set()
            if dfs(0, 0, m):
                ans = m 
                l = m + 1
            else:
                r = m - 1

        return ans