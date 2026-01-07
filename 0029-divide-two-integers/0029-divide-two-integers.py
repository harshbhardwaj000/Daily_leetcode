class Solution(object):
    def divide(self, dividend, divisor):
        
        maxx = 2**31 -1
        minn = -2**31

        if dividend == minn and divisor == -1:
            return maxx
        
        sign = -1 if (dividend < 0)^(divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)

        ans = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= (divisor << shift):
                shift +=1
            ans +=1 << (shift -1)
            dividend -= divisor << (shift -1)
        return sign*ans

        