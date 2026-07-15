class Solution(object):
    def gcdOfOddEvenSums(self, n):
        # count_odd =0
        # count_even=0
        # for i in range(n*2):
        #     if i%2 == 0:
        #         count_even += i
        #     else:
        #         count_odd += i
        # return count_odd - count_even
        
        return sum(i if i%2!=0 else -i for i in range(n*2))