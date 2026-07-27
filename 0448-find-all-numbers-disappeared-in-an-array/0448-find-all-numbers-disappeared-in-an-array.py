class Solution(object):
    def findDisappearedNumbers(self, nums):
        # n= len(nums)
        # res=[]
        # for i in range(1,n+1):
        #     if i not in nums:
        #         res.append(i)
        # return res
        s = set(nums)
        return [ i for i in range(1,len(nums)+1) if i not in s]

        