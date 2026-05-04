class Solution(object):
    def check(self, nums):
        # m="".join(map(str,sorted(nums)))        # "12345"
        # num ="".join(str(x) for x in nums)      # "34512"
        # return m in (num+num)
        n=len(nums)
        count =0
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                count+=1
        return count <=1
        


        