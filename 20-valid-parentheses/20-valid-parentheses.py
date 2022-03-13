class Solution:
    def isValid(self, s: str) -> bool:
        pmap = {
            '{': '}', '(': ')', '[':']'
        }         
        stack = []
        for i in s:
            if len(stack)==0 and i in pmap.values():
                return False
            if i in pmap.keys():
                stack.append(i)
            elif i != pmap[stack.pop()]:
                return False            
        if len(stack) != 0:
            return False
        return True
