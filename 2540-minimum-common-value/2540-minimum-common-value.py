class Solution(object):
    def getCommon(self, nums1, nums2):
        left =0
        right=0
        n1=len(nums1)
        n2=len(nums2)
        while left < n1 and right < n2:
            if nums1[left] == nums2[right]:
                return nums1[left]
            if nums1[left] > nums2[right]:
                right+=1
            else:
                left+=1
        return -1
        

        
        