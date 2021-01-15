class Solution:
    def myPow(self, x, n):
        val = 1
        if n < 0:
            x = 1 / x
        n = abs(n)
        n = bin(n)[2:]
        
        for i in range(len(n)):
            b = n[::-1][i]
            if b == '1':
                val *= x
            x = x**2
            
        return val