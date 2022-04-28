class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0;
        for i in range(len(nums)):#(int i=0; i<nums.size(); i++){
            if reachable < i:   return False;
            
            reachable  = max(reachable, i+nums[i]);
        
        return True;