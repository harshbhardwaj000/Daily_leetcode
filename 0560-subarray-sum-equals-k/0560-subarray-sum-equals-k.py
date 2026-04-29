from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        # count =  0
        # n=len(nums)
        # for i in range(n):
        #     summ=0
        #     for j in range(i,n):
        #         summ+=nums[j]
        #         if summ == k:
        #             count+=1
        # return count
        sun,count = 0,0
        d = collections.defaultdict(int)
        d[0] = 1
        for i in range(len(nums)):
            sun += nums[i]
            if sun -k in d:
                count+= d[sun-k]
            d[sun]+=1
        return count

