class Solution(object):
    def maxVowels(self, s, k):
        vol="aeiou"
        count=0
        for i in range(k):
            if s[i] in vol:
                count+=1
        max_count=count
        for i in range(k,len(s)):
            if s[i] in vol:
                count+=1
            if s[i-k] in vol:
                count -=1
            max_count=max(max_count,count)
        return max_count

        