from collections import Counter
class Solution(object):
    def countWords(self, words1, words2):
        count1=Counter(words1)
        ans=[x for x in words1 if count1[x] <= 1] #["leetcode","amazing","as"]
        
        count2=Counter(words2)
        ans1=[x for x in words2 if count2[x] <=1] #["amazing","leetcode","is"]
        
        count=0
        for X in ans:
            if X in ans1:
                count+=1
        return count


        
        