class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None:
            return(0)
        length = len(nums)
        if length == 0 or length == 1:
            return (length)
        count = length - 1
        newlength = length
        while count > 0 :
            if nums[count] == nums[count-1]:
                del nums[count]
                newlength -= 1
            count = count-1 
        return len(nums)