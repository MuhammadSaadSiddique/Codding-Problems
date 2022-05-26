class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        i = 0
        while i < 32:
            if n&1 == 1:
                count+=1
            n = n >>1
            i+=1
        return count
        """
        space: O(1)
        time: O(32) ~ O(1)
        """