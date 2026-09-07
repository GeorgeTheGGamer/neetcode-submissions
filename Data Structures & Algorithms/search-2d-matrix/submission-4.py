class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      
        # To achieve O(log(m*n)) must have all within the while loop

        leftRow = 0
        rightRow = len(matrix) - 1

        targetRow = 0

        l = 0
        r = len(matrix[0]) - 1

        # Search the rows
        while leftRow <= rightRow:
            middleRow = (leftRow+rightRow) // 2
            if target > matrix[middleRow][-1]:
                leftRow = middleRow + 1
            elif target < matrix[middleRow][0]:
                rightRow = middleRow - 1
            elif target >= matrix[middleRow][0] and target <= matrix[middleRow][-1]:
                targetRow = middleRow
                break
            else:
                return False

        # Search the columns within the row
        while l <= r:
            m = (l+r) // 2
            if target > matrix[targetRow][m]:
                l = m + 1
            elif target < matrix[targetRow][m]:
                r = m - 1
            elif target == matrix[targetRow][m]:
                return True
            else:
                return False

        
        return False

