class Solution(object):
    def merge(self, nums1, m, nums2, n):
        arr=[]
        for val in nums1[:m]: 
            arr.append(val)
        for val2 in nums2:
            arr.append(val2)
        arr.sort()
        for i in range(len(arr)):
            nums1[i]= arr[i]
        return nums1


