class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        d = {0:-1}
        sum_ = 0
        
        for i,a in enumerate(nums):
            sum_ += a
            if sum_ % k in d and i - d[sum_ % k] >= 2: # if sum%k is already in dict (at some index left) means remainder is 0 when dividing sum(left...i) by k
                return True
            
            if sum_ % k not in d: # record index for this remainder
                d[sum_ % k] = i
                
        return False