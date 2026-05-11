class Solution(object):
    def separateDigits(self, nums):
        arr = []
        for num in nums:
            for dig in str(num):
                arr.append(int(dig))
        return arr
        