class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        p=nums[0]
        c=0
        for n in range(1,len(nums)):
            if(nums[n]==p):
                c+=1 
            p=nums[n]
            if c>0:
                return True 
        return False