class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = 1
        i=0     #power
        while(num <= n):
            num = 2**i
            i += 1
            if(num == n):
                return True
            
        return False