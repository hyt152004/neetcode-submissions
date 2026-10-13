class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # for every single grid val, if its 1 and not seen
            # update island count
            # will call bfs

        row = len(grid)
        col = len(grid[0])
        islands = 0
        visited = set()

        def bfs(bfsRow, bfsCol):
            grid[bfsRow][bfsCol] == "0"

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            q = deque([(bfsRow, bfsCol)])

            while q:
                qRow, qCol = q.popleft()

                for dr, dc in directions:
                    newRow = qRow + dr
                    newCol = qCol + dc

                    if newRow in range(row) and newCol in range(col) and grid[newRow][newCol] == "1":
                        q.append((newRow, newCol))
                        grid[newRow][newCol] = "0"


        for r in range(row):
            for c in range(col):
                gridVal = grid[r][c]

                if gridVal == "1":
                    islands += 1
                    bfs(r, c)


        # return island count
        return islands