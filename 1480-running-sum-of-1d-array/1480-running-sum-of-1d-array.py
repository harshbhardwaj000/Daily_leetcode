class Solution(object):
    def runningSum(self, nums):
        prefix = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        return prefix[1:]
        


        