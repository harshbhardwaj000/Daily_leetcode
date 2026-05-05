from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        count = Counter(nums)
        for key,value in count.items():
            if value > 1:
                return True
        return False
        