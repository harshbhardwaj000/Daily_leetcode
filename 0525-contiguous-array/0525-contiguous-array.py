class Solution(object):
    def findMaxLength(self, nums):
        zero,one=0,0
        res=0
        dic={}
        for i,n in enumerate(nums):
            if n ==0:
                zero+=1
            else:
                one+=1
            if one-zero not in dic:
                dic[one-zero]=i
            if one == zero:
                res=one+zero
            else:
                idx= dic[one-zero]
                res=max(res,i-idx)
        return res

