class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # do two binary search 

        # first to figure out which row to search

        # second to figure out which col its in


        bottom = 0
        top = len(matrix) - 1
        rowLength = len(matrix)
        colLength = len(matrix[0])

        # cases
        # need to find row where the range will include target

        # if target falls lower, go up more

        # if target is higher, go down more
        targetRowIndex = -1

        while bottom <= top:
            mid = (bottom + top) // 2

            if matrix[mid][0] <= target and target <= matrix[mid][colLength - 1]:
                targetRowIndex = mid
                break

            elif target < matrix[mid][0]:
                top = mid - 1
            else:
                bottom = mid + 1

        if targetRowIndex == -1:
            return False


        left = 0
        right = colLength
        targetRow = matrix[targetRowIndex]

        while left <= right:
            mid = (left + right) // 2
            midVal = targetRow[mid]

            if midVal == target:
                return True

            elif midVal > target:
                right = mid - 1
            else:
                left = mid + 1



        return False









