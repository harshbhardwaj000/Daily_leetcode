class Solution(object):
    def detectCapitalUse(self, word):
        up = 0
        low = 0
        for x in word:
            if x.isupper():
                up +=1
            elif x.islower():
                low +=1
        if (word[0].isupper() and up < 2) or (up > 0 and low <= 0) or (up <=0 and low > 0):
            return True
        # elif 
        #     return True
        # elif 
        #     return True
        else:
            return False

        