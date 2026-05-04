class Solution(object):
    def maxRotateFunction(self, nums):
        n=len(nums)
        total=sum(nums)
        
        f= sum(i*num for i,num in enumerate(nums))
        max_val = f

        for k in range(1,n):
            f = f + total - n * nums[-k]
            max_val = max(max_val,f)
        return max_val
        