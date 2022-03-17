class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        finalArr = nums1 + nums2
        finalArr.sort()
        length = len(finalArr)
        if length % 2 == 0:
            index = int(length / 2)
            return ((finalArr[index] + finalArr[index -1]) / 2)
        else:
            index = int(length / 2)
            return finalArr[index]
        