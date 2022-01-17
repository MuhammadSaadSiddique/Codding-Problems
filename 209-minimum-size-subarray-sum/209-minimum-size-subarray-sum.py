import sys
class Solution:
    def minSubArrayLen(self, target: int, A: List[int]) -> int:
        i, res = 0, len(A) + 1
        s=target
        for j in range(len(A)):
            s -= A[j]
            while s <= 0:
                res = min(res, j - i + 1)
                s += A[i]
                i += 1
        return res % (len(A) + 1)