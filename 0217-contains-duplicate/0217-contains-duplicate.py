from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        count = Counter(nums)
        return any(val > 1 for val in count.values())
            
        