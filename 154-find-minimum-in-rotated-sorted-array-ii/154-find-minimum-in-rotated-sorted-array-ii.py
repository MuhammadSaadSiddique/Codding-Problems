class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            
            # skip duplicates
            while left < mid and nums[left] == nums[mid]:
                left += 1
            while right > mid and nums[right] == nums[mid]:
                right -= 1
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]