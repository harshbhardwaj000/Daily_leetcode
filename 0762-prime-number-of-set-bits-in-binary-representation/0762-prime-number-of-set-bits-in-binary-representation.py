class Solution(object):
    def countPrimeSetBits(self, left, right):
        def prime(n):
            if n<=1:
                return False
            for i in range(2,n):
                if n % i ==0:
                    return False
            return True
        result = 0
        for i in range(left,right+1):
            count = bin(i).count('1')

            if prime(count):
                result +=1
        return result 
            

        