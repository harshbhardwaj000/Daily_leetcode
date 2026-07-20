from fractions import gcd
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        count_odd =0
        count_even=0
        for i in range(n*2):
            if i%2 == 0:
                count_even += i
            else:
                count_odd += i
        return gcd(count_even,count_odd)
        
        