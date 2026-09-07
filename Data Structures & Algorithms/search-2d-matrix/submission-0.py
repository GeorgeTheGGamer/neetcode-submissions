class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(m * n), binary search on each level

        array = []
        for m in range(len(matrix)):
            for n in range(len(matrix[m])):
                array.append(matrix[m][n])
        
        l = 0
        r = len(array) - 1

        while l <= r:
            m = (l+r) // 2
            if target > array[m]:
                l = m + 1
            elif target < array[m]:
                r = m - 1
            else:
                return True

        return False       
        