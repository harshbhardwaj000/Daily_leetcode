class Solution(object):
    def missingMultiple(self, nums, k):
        maxx= max(nums)
        num= maxx * k
        for i in range(1,num+2):
            if i % k == 0:
                if i not in nums:
                    return i
        