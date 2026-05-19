class Solution(object):
    def intersect(self, nums1, nums2):
        arr=[]
        tem=nums2[:]
        for x in nums1:
            if x in tem:
                arr.append(x)
                tem.remove(x)
        return arr
        