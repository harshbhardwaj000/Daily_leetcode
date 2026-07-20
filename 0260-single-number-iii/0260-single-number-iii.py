from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        res = []
        count = Counter(nums)
        for key,value in count.items():
            if value < 2:
                res.append(key)
        return res

        