class Solution(object):
    def maxProduct(self, n):
        res=[]
        mul = 0
        for d in str(n):
            res.append(int(d))
        n= len(res)
        res.sort()
        mul = res[n-1] * res[n-2]
        return mul
        

