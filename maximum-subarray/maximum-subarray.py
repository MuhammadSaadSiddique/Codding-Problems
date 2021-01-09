class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        dp = [0]*length                 
        #print(dp)
        for i,num in enumerate(nums): 
            #print(dp[i-1])
            dp[i] = max(dp[i-1] + num, num)
        #print(dp)
        return max(dp)
