from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # questions:
        # can grid be empty? will have at least one element
        # can I assume each inner grid is the same size? yes
        # what about 1's diagonally? not part of the same island
        # can i assume the grid consists of only 1's and 0's
        

        # note: 
        # the grid consists of STRINGS not INT

        # brute force:
        # use a set to keep track of all 1's index

        # loop again and check to see if the set contains any other 1's 
            # as you move, remove the elements from the set
            # use a queue to keep track of all the directions to go

        # time: O(n)
        # space: O(n)

        # solution -> brute force

        # somehow track all the 1's we've seen
        rowLength = len(grid)
        colLength = len(grid[0])
        islands = 0

        def bfs(bfs_row, bfs_col):
            bfs_grid_val = grid[bfs_row][bfs_col]

            q = deque([(bfs_row, bfs_col)])

            while q:
                for _ in range(len(q)):
                    q_row, q_col = q.popleft()

                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                    for d_r, d_c in directions:
                        new_r = q_row + d_r
                        new_c = q_col + d_c

                        # is it 1? have we seen it? is the row and col in range with grid?
                        if new_r in range(rowLength) and new_c in range(colLength) and grid[new_r][new_c] == '1':
                            q.append((new_r, new_c))
                            grid[new_r][new_c] = '0'


        for r in range(rowLength):
            for c in range(colLength):
                gridVal = grid[r][c]
                if gridVal == '1':
                    bfs(r, c)
                    islands += 1


        # return the number of islands
        return islands


        # time o(mn)
        # space o(mn)




