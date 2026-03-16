class Solution(object):
    def countCommas(self, n):
        total = 0
        i= 1000
        while i <= n:
            total += n-i+1
            i *= 1000
        return total
                