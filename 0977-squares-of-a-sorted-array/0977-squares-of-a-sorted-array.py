class Solution(object):
    def sortedSquares(self, nums):
        n=len(nums)
        i=0
        j=n-1
        k=n-1
        res=[0]*n
        while (i <= j):
            l=nums[i]* nums[i]
            r=nums[j]*nums[j]
            if l > r:
                res[k]=l
                i+=1
            else:
                res[k]=r
                j-=1
            k-=1
        return res

        