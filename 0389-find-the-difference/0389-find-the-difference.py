class Solution(object):
    def findTheDifference(self, s, t):
        m=list(s)
        n=list(t)
        for val in n:
            if val in m:
                m.remove(val)
            else:
                return val

        