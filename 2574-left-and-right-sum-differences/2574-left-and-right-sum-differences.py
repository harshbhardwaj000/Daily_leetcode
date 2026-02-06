class Solution(object):
    def leftRightDifference(self, nums):
        total=sum(nums)
        lsum=0
        result=[]
        for i in range(len(nums)):
            rsum=total-lsum-nums[i]
            result.append(abs(lsum-rsum))
            lsum+=nums[i]
        return result


        
      
            



        
        