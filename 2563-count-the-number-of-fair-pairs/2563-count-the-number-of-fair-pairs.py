class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        def binary(l,r,target):
            while l <= r:
                mid = (l+r)//2  ### l+(r-l)//2
                if nums[mid] >= target:
                    r= mid-1
                else:
                    l= mid+1        
            return r
        nums.sort()
        res = 0
        for i in range(len(nums)):
            low = lower - nums[i]
            up = upper - nums[i]
            res += (
                binary(i+1,len(nums)-1,up+1) - binary(i+1,len(nums)-1,low)
            )
        return res
        
        