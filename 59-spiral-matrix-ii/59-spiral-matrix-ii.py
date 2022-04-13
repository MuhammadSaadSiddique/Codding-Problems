class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [n*[0] for i in range(n)]
        
        nlayers = (n+1) // 2
        cnt = 1
        
        for layer in range(nlayers):
            #Direction 1: from top left to top right
            for i in range(n-2*layer):
                result[layer][i+layer] = cnt
                cnt+=1
            
            #Direction 2: from top right to bottom right
            for j in range(n-2*layer - 1):
                result[layer+1+j][-layer-1] = cnt
                cnt +=1
            
            #Direction 3: from bottom right to bottom left
            for i in range(n-2*layer-1):
                result[-layer-1][-layer-2-i] = cnt
                cnt +=1
            
            #Direction 4: from bottom left to top left
            for j in range(n - 2 *layer - 2):
                result[-layer-2-j][layer] = cnt
                cnt +=1
            
        
        return result
            
        
        