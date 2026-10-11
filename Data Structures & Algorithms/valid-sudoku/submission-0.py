class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        # idea:
        # have a set for each row
        # have a set for each column
        # have a set for each sub-box

        # use a hashmap to store each row/column/sub-box as key 
        # and set as the value

        # each time we visit a number on sudoku,
        # check, O(1), whether a duplicate exists for its row, column and sub-box

        # sub-box index is determined by index // 3 (floor division)

        # a dictionary with a default value of a set.
        # don't have to handle cases where the key doesn't exists
        # can just .add for set
        # can just .append for list
        rows = defaultdict(set)
        cols = defaultdict(set)
        # need to be slight diff
        # need to be a 2d 
        # key: (row, col)
        subBoxes = defaultdict(set)

        # visit each number on sudoku.
        # i is the row
        # j is the col
        for i in range(9):
            for j in range(9):
                currentVal = board[i][j]
                if currentVal == ".":
                    continue
                
                if (currentVal in rows[i] or currentVal in cols[j] or currentVal in subBoxes[(i // 3, j // 3)]):
                    return False

                rows[i].add(currentVal)
                cols[j].add(currentVal)
                subBoxes[(i // 3, j // 3)].add(currentVal)

        return True




