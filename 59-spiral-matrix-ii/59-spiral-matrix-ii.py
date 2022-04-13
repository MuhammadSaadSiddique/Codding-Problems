class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        cnt=1
        res=[ [0 for i in range(n)] for j in range(n) ]  
        
        #res.append([i for i in range(1,n+1)])
        for layer in range(int((n+1)/2)):
            for ptr in range(layer,n-layer):
                res[layer][ptr]=cnt
                cnt+=1
            for ptr in range(layer+1,n-layer):
                res[ptr][n-layer-1]=cnt
                cnt+=1
            for ptr in range(layer+1,n-layer):
                res[n-layer-1][n-ptr-1]=cnt
                cnt+=1
            for ptr in range(layer+1,n-layer-1):
                res[n-ptr-1][layer]=cnt
                cnt+=1
            
        return res
            
        
        