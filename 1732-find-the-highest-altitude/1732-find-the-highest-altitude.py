class Solution(object):
    def largestAltitude(self, gain):
        maxx = 0
        i=0
        for j in gain:
            maxx+=j
            i=max(i,maxx)
        return i
        
                



        