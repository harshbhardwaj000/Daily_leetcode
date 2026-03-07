class Solution(object):
    def sortedSquares(self, nums):
        result=[]
        for i in range(len(nums)):
            result.append(nums[i]**2)
        result.sort()
        return result

        