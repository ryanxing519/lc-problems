class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        N, M = len(grid), len(grid[0])

        queue = []

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    queue.append((i, j))

        dist = 0
        graph = [[float("inf")] * M for _ in range(N)]

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                graph[x][y] = dist
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (
                        (0 <= nx <= N - 1)
                        and (0 <= ny <= M - 1)
                        and graph[nx][ny] > dist + 1
                    ):
                        queue.append((nx, ny))
            dist += 1

        # dfs and check every single path
        def dfs(x, y, max_dist):

            if (
                not (0 <= x <= N - 1)
                or not (0 <= y <= M - 1)
                or graph[x][y] > max_dist
                or (x, y) in visited
            ):
                return False

            if x == N - 1 and y == M - 1:
                return True

            visited.add((x, y))

            return (
                dfs(x + 1, y, max_dist)
                or dfs(x - 1, y, max_dist)
                or dfs(x, y + 1, max_dist)
                or dfs(x, y - 1, max_dist)
            )

        l, r = 0, N

        while l <= r:
            m = (l + r) // 2 + 1
            visited = set()
            if dfs(0, 0, m):
                l = m
            else:
                r = m - 1

        return l
