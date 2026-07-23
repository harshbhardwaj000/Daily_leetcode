from collections import defaultdict
class Solution(object):
    def totalFruit(self, fruits):
        i = 0
        res = 0
        count = defaultdict(int)
        for j in range(len(fruits)):
            count[fruits[j]]+= 1
            while len(count) > 2:
                count[fruits[i]]-= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i+=1 
            res = max(res,j-i+1)
        return res