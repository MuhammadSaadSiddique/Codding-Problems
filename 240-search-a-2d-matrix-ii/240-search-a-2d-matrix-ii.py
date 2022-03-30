class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        def helper(lp: int, rp: int, up: int, dp: int) -> bool:
            if lp > rp or up > dp:
                # NO DIMENSION
                return False
            
            if target < matrix[up][lp] or target > matrix[dp][rp]:
                # SMALLER THAN TOP LEFT OR GRATER THAN BOTTOM RIGHT
                return False
            
            mid = (lp + rp) // 2
            
            # BINARY SEARCH
            stop = False
            lower, higher = up, dp
            while not stop:
                if lower == higher:
                    stop = True
                row = (lower + higher) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    lower = row + 1
                else:
                    higher = row
            if matrix[row][mid] < target and row <= dp:
                row += 1

            return helper(lp, mid - 1, row, dp) or helper(mid + 1, rp, up, row - 1)
            

        return helper(0, m - 1, 0, n - 1)