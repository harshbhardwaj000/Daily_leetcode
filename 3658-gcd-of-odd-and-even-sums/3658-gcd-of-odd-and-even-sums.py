class Solution(object):
    def gcdOfOddEvenSums(self, n):
        count_even=0
        for i in range(n*2):
            if i%2 != 0:
                count_even += i
            else:
                count_even -= i
        return count_even
        
        