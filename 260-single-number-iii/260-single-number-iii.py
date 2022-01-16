class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = [None,None]
        a = 0
        
        for i in nums:
            if(nums.count(i) == 1):
                ans[a] = i
                a+=1
            if(ans[1] != None):
                break
        
        return ans