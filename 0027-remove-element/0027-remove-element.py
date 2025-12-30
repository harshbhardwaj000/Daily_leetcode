class Solution(object):
    def removeElement(self, nums, val):
        m=len(nums)
        k=0
        for i in range(m):
            if nums[i] !=val:
                nums[k]=nums[i]
                k +=1
        return k

        