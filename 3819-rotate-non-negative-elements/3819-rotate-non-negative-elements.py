class Solution(object):
    def rotateElements(self, nums, k):
        arr=[x for x in nums if x >= 0]
        
        n=len(arr)
        if n ==0:
            return nums

        k = k % n
        arr = arr[k:] + arr[:k]

        j = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                nums[i] = arr[j]
                j+=1
        return nums
            
        