class Solution(object):
    def reverseWords(self, s):
        
        s = s.split()
        s.reverse()
        anss= " ".join(s)
        return anss