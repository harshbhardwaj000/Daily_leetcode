class Solution(object):
    def numberOfSpecialChars(self, word):
        count = 0
        up=set()
        low=set()
        for x in word:
            if x.isupper():
                up.add(x)
            elif x.islower():
                low.add(x)
        for x in low:
            if x.upper() in up:
                count+=1
        return count
        