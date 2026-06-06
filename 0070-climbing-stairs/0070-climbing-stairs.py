class Solution(object):
    def climbStairs(self, n):
        if (n == 0) or (n == 1):
            return 1
        pre =1
        pre_pre=1
        for i in range(2,n+1):
            curr = pre + pre_pre  ## 2
            pre_pre = pre
            pre=curr
        return curr

        