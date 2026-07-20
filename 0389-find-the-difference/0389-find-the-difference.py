from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        count_s = Counter(s)
        count_t = Counter(t)
        for key in count_t:
            if key in count_s:
                if count_t[key] != count_s[key]:
                    return key
            elif key not in count_s:
                return key
            
