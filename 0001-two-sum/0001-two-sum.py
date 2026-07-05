class Solution(object):
    def twoSum(self, nums, target):
        # left =0
        # right=len(nums)-1

        # while (left < right):
        #     if left - target > right:
        #         left+=1
        #     elif right - target < left:
        #         right+=1
        #     elif left + right == target:
        #         return [left,right]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        