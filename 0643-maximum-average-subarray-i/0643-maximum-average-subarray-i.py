class Solution(object):
    def findMaxAverage(self, nums, k):
        summ=sum(nums[:k])
        count=summ
        for i in range(k,len(nums)):
            summ+=nums[i]
            summ-=nums[i-k]
            if summ>count:
                count=summ
        return count/float(k)
            
        
        