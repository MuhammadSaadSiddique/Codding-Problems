class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        for n in nums:
            if original==n:
                return self.findFinalValue(nums,original*2)
        return original