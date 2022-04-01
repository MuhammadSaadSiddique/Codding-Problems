class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        j=0
        i=-1
        while j<len(s)/2:
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
            j+=1
            i-=1