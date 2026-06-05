class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        n= len(nums)
        k=0
        summ = 0
        while k!=n:
            summ = summ+nums[k]
            k+=2
        return summ

        