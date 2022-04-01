class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        j=0
        i=len(s)-1
        while j<i:
            temp=s[i]
            s[i]=s[j];
            s[j]=temp
            j+=1
            i-=1
        print(s)