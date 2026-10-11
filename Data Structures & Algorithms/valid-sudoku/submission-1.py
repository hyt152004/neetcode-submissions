from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create a set for each row and column?
            # not efficient

        # create a hashmap every row
        # create a hashmap every column
        # create a hashmap for every box
            # (r // 3, c // 3)
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        boxMap = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                val = board[row][col]
                if val == ".":
                    continue

                if val in rowMap[row]:
                    return False
                if val in colMap[col]:
                    print("col")
                    return False
                if  val in boxMap[(row // 3, col // 3)]:
                    print("box")
                    return False
                rowMap[row].add(val)
                colMap[col].add(val)
                boxMap[(row // 3, col // 3)].add(val)

        return True

        

