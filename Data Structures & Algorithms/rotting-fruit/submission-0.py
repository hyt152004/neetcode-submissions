from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        rowLength = len(grid)
        colLength = len(grid[0])

        rotten = []
        fresh = 0

        time = 0
        


        for r in range(rowLength):
            for c in range(colLength):
                gridVal = grid[r][c]

                if gridVal == 2:
                    rotten.append((r, c))
                elif gridVal == 1:
                    fresh += 1

        q = deque(rotten)

        while q and fresh > 0:
            for _ in range(len(q)):
                qRow, qCol = q.popleft()

                directions = [(1,0),(-1,0),(0,1),(0,-1)]

                for dr, dc in directions:
                    newRow = qRow + dr
                    newCol = qCol + dc
                    if newRow in range(rowLength) and newCol in range(colLength) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        q.append((newRow, newCol))
                        fresh -= 1
            time += 1
        
        if fresh:
            return -1

        return time









