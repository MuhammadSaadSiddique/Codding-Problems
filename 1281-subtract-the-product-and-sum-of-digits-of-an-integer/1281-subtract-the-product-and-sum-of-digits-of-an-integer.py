class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1  
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit
            prod*=digit
        
        return prod-total_sum