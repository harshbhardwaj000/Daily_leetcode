from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        word = s1.split() + s2.split()
        count= Counter(word)
        arr=[]
        for X in count:
            if count[X] == 1:
                arr.append(X)
        return arr

        

        