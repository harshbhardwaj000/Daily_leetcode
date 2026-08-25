class Solution(object):
    def missingMultiple(self, nums, k):
       
        for i in range(1,(max(nums)*k)+2):
            if i % k == 0:
                if i not in nums:
                    return i
        