class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        res = []
        mix = max(candies)
        for x in candies:
            if (x + extraCandies) >=  mix:
                res.append(True)
            else:
                res.append(False)
        return res
        