class Solution(object):
    def missingMultiple(self, nums, k):
        num = set(nums)
        for i in range(k,max(nums)*k+2,k):
            if i not in num:
                return i
        