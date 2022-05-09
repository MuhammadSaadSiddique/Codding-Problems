class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        alphabets = [chr(x) for x in range(ord('a'),ord('z')+1)]
        numsWithFourLetters = [7,9]
        
        valueMap = {}
        for i in range(9, 1, -1):
            valueMap[i] = [alphabets.pop() for x in range(4 if i in numsWithFourLetters else 3)]
        
        result = []
        for digit in digits:
            result = self.combine(result, valueMap[int(digit)])
            
        return result
    
    def combine(self, list1, list2):
        result = []
        if len(list1) == 0:
            return list2
        
        for element1 in list1:
            for element2 in list2:
                result.append(element1+element2)
        return result