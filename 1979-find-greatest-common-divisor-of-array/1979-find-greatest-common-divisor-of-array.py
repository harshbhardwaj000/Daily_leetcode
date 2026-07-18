class Solution(object):
    def findGCD(self, nums):
        nums.sort()
        n=len(nums)
        re=[]
        for i in range(1,max(nums)+1):
            if nums[0] % i==0 and nums[n-1] % i ==0:
                re.append(i)
        return max(re)

        