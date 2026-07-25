class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        count = 0
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                for k in range(j,n):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        count +=1
        return count
        