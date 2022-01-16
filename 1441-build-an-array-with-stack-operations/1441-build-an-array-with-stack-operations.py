class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output=[]
        
        for i in range(1,n+1):
            if i in target:
                output.append("Push")
            else:
                output.append("Push")
                output.append("Pop")
            
            if i==target[-1]:
                break
        
        return output