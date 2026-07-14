class Solution(object):
    def rob(self, nums):
        n=len(nums)
        dp=[0]*(n+1)
        # t=len(dp)
        dp[n-1]=nums[n-1]
        dp[n-2]= max(nums[n-2],nums[n-1])
        for i in range(n-3,-1,-1):
            dp[i]=max(nums[i]+dp[i+2],dp[i+1])
        return dp[0]
        