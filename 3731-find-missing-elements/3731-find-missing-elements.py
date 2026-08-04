class Solution(object):
    def findMissingElements(self, nums):
        mi = min(nums)
        ma= max(nums)
        n=len(nums)
        res=[]
        for i in range(mi,ma):
            if i not in nums:
                res.append(i)
        return res
            # if len(res) == 0:
            #     return []


        