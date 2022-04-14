class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0];
        dp_im2 = nums[0];
        dp_im1 = max(nums[0], nums[1]);
        dp_i = dp_im1;
        
        for i in range(2,len(nums)):
            dp_i = max(nums[i]+dp_im2, dp_im1);
            dp_im2 = dp_im1;
            dp_im1 = dp_i;
        
        return dp_i;