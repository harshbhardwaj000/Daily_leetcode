class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        arr = nums1 + nums2
        arr.sort()
        n = len(arr)
        if n % 2 == 1:
            return arr[n//2]
        else:
            mid1 = arr[n//2]
            mid2 = arr[n//2-1]
            return (mid1 + mid2)/2.0

        