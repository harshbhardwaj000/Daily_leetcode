from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        count = float('inf')
        count1= Counter(text)
        count2= Counter("balloon")

        for ch in count2:
            count =min(count, count1[ch] // count2[ch])
        return count
        


        
        