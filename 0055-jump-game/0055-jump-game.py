class Solution(object):
    def canJump(self, nums):
        n=len(nums)
        max_in = 0
        for i in range(n):
            if i > max_in:
                return False
            max_in=max(max_in,i+nums[i])
        return True

        