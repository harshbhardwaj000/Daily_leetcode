class Solution(object):
    def intersection(self, nums1, nums2):
        arr=[]
        for x in nums1:
            for y in nums2:
                if x == y:
                    arr.append(x)
            s=list(set(arr))
        return s
        