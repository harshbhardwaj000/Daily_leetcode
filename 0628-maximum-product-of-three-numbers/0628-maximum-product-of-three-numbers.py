class Solution(object):
    def maximumProduct(self, nums):
        # max_multiple = float('-inf')
        # n=len(nums)
        # for i in range(n):
        #     for j in range(i):
        #         for k in range(j):
        #             mul = nums[i] * nums[j] * nums[k]
        #             if mul  > max_multiple:
        #                 max_multiple = max(max_multiple, mul)
        # return max_multiple
        nums.sort()
        result = max(nums[0]*nums[1]* nums[-1], nums[-1]* nums[-2]* nums[-3])
        return result
        