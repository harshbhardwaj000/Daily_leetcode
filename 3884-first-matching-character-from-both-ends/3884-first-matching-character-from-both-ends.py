class Solution(object):
    def firstMatchingIndex(self, s):
        n= len(s)
        if n == 1:
                return 0
        for i in range(n-1):
            if s[i] == s[n - i - 1]:
                return i
        return -1
        