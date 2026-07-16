class Solution(object):
    def pivotIndex(self, nums):
        l_sum=0
        r_sum=0
        total =sum(nums)
        for i in range(len(nums)):
            r_sum = total-l_sum - nums[i]
            if r_sum == l_sum:
                return i
            else:
                l_sum += nums[i]
        return -1
        
        