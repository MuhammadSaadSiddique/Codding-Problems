class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        rows, cols = len(grid), len(grid[0])
        res = [[0] * cols for _ in range(rows)]
		
        for r in range(rows):
            for c in range(cols):
                pos = (r * cols + c + k) % (rows * cols)
                _r, _c = divmod(pos, cols)
                res[_r][_c] = grid[r][c]
				
        return res
        