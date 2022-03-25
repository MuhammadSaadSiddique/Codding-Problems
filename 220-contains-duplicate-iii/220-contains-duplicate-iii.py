class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums or t < 0 or k <= 0: return False
        width, l, dt = t+1, len(nums), {}
        for i in range(l):
            pos = nums[i] // width
            if pos in dt: return True
            if pos-1 in dt and nums[i] - dt[pos-1] < width: return True
            if pos+1 in dt and dt[pos+1] - nums[i] < width: return True
            dt[pos] = nums[i]
            if i >= k: del dt[nums[i-k] // width]
        return False