from collections import Counter
class Solution(object):
    def intersection(self, nums):
        n=len(nums)
        common = []
        max_val =0
        count = Counter(x for row in nums for x in row)
        for x in count:
            if count[x] == n:
                common.append(x)
        common.sort()
        return common

        