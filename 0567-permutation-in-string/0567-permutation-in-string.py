class Solution(object):
    def checkInclusion(self, s1, s2):
        from collections import Counter
        k= len(s1)
        s1_count = Counter(s1)
        for i in range(len(s2)-k +1):
            if Counter(s2[i:i+k])==s1_count:
                return True
        return False

                    
                

