class Solution(object):
    def firstMatchingIndex(self, s):
        n= len(s) if 1 return 0
        
        for i in range(len(s)-1):
            if s[i] == s[n - i - 1]:
                return i
        return -1
        