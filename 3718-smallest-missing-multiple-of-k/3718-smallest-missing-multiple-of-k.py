class Solution(object):
    def missingMultiple(self, nums, k):
        num = set(nums)
        for i in range(1,max(nums)*k+2):
            if i % k == 0:
                if i not in num:
                    return i
        