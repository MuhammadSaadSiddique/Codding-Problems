class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums=[]
        for w in s.split():
            if w.isdigit():
                nums.append(int(w))
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                return False
                       
        return True
                   