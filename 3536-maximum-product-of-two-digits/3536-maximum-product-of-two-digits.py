class Solution(object):
    def maxProduct(self, n):
        res=[]
        mul = 0
        for d in str(n):
            res.append(int(d))
        res.sort()
        mul = res[-1] * res[-2]
        return mul
        

