class Solution(object):
    def maxSubArray(self, nums):
        count=nums[0]
        max_count=nums[0]
        for num in nums[1:]:
            count=max(num,count+num)
            max_count=max(max_count,count)
        return max_count
        
