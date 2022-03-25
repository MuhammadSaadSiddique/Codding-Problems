class Solution:
    def prsum(self,num,count=0) -> int:
        
        if(num==4):
            return count+2
        if(num%2==0):
            return self.prsum(num/2,count+1)
        else:
            return self.prsum(3*num+1,count+1)
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        maxi={}
        for i in range(lo,hi+1):            
            maxi.update({i:self.prsum(i,0)})
        maxi = sorted(maxi.items(), key=lambda x:x[1])
        
        print(maxi)
        return maxi[k-1][0]
        