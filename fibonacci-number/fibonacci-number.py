class Solution:
    
    def fib(self, n: int) -> int:
        if n <=1:
            return n
        
        fib = [0 for i in range(n+1)]
        fib[0], fib[1], fib[2]=0,1,1
        #if fib[n]==0:
        for i in range(3, n+1):
            fib[i] = fib[i-1]+fib[i-2]
        print(fib)
        return fib[-1]
        
    