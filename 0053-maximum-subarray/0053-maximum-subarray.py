class Solution(object):
    def maxSubArray(self, nums):
        submax=nums[0]
        cursum=0
        for x in nums:
            if cursum < 0:
                cursum =0
            cursum +=x
            submax=max(submax,cursum)
        return submax
        