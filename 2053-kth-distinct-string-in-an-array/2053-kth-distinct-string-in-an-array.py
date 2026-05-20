from collections import Counter
class Solution(object):
    def kthDistinct(self, arr, k):
        count=Counter(arr) #{d:1,b:2,c:2,a:1}
        ar=[]
        for x in arr:
            if count[x] == 1: 
                ar.append(x) #[d,a]
        if len(ar) < k:
            return ""
        else:
            return ar[k-1]
        