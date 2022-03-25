class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        p=nums[0]
        c=-1
        for n in nums:
            print(p)
            if(n==p):
                c+=1
               
            p=n
            if c==1:
                return True 
        return False