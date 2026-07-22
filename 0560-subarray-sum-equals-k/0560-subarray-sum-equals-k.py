from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        cur_sum = 0
        d = defaultdict(int)
        d[0]=1
        for i in range(len(nums)):
            cur_sum += nums[i]
            if  cur_sum  - k in d:
                count += d[cur_sum - k]
            d[cur_sum]+=1
        return count