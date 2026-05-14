from collections import Counter
class Solution(object):
    def isGood(self, nums):
        c=Counter(nums)
        n=max(nums)
        if len(nums) != n+1:
            return False
        for i in range(1,n):
            if c[i] !=1:
                return False
        if c[n] !=2:
            return False
        return True
        