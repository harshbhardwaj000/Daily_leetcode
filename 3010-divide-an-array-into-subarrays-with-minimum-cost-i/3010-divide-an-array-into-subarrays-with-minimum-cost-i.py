class Solution(object):
    def minimumCost(self, nums):
        firstcost = nums[0]
        rest = nums[1:]
        rest.sort()
        return firstcost + rest[0] + rest[1]
        