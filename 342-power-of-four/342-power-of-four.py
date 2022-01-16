class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        num = 1
        i=0     #power
        while(num <= n):
            num = 4**i
            i += 1
            if(num == n):
                return True
            
        return False