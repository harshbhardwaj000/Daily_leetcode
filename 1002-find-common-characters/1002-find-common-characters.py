from collections import Counter
class Solution(object):
    def commonChars(self, words):
        count=Counter(words[0])
        for wor in words[1:]:
            count &=Counter(wor)
        return list(count.elements())
        


        