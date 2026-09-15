class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Search question
        # log -> splitting the search base
        # Binary Search
        # log(mn) = log(m) + log(n)
        # So we cut down the rows m first
        rowLeft = 0
        rowRight = len(matrix) - 1

        targetRow = None

        while rowLeft <= rowRight:
            m = (rowLeft+rowRight) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                targetRow = m
                break
            elif target < matrix[m][-1]:
                rowRight = m-1
            elif target > matrix [m][-1]:
                rowLeft = m+1
        
        if targetRow == None:
            return False

        # Then cut down the column within the row
        columnLeft = 0
        columnRight = len(matrix[targetRow])
        while columnLeft <= columnRight:
            m = (columnLeft + columnRight) // 2
            if matrix[targetRow][m] == target:
                return True
            elif target < matrix[targetRow][m]:
                columnRight = m - 1
            elif target > matrix[targetRow][m]:
                columnLeft = m + 1
        
        return False


        