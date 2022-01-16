class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        start = 0
        end = len(nums) - 1
        middle = (end + start) // 2
        
        while start <= end:
            
            if nums[middle] < target:
                start = middle + 1
                
            elif nums[middle] > target:
                end = middle - 1
            
            else:
                
                if nums[start] == target and nums[end] == target:
                    result = [start, end]
                    break
                
                if nums[start] < target:
                    start += 1
                
                if nums[end] > target:
                    end -= 1
            
            middle = (end + start) // 2
            
        return result