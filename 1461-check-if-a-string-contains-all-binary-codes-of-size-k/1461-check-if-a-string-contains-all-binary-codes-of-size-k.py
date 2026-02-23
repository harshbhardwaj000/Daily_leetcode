class Solution(object):
    def hasAllCodes(self, s, k):
        seen = set()
        target = 2**k

        for i in range(len(s)-k+1):
            seen.add(s[i:i+k])
            if len(seen) == target:
                return True
        return False
        
        
        

        