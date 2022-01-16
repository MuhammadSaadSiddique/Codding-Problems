class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #ans = [None,None]
        #a = 0
        
        for i in nums:
            if(nums.count(i) == 1):
                return i
                
        
        return 0