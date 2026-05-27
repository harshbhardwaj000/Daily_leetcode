class Solution(object):
    def capitalizeTitle(self, title):
        s= title.lower().split() ####["hello","world"]
        for i in range(len(s)):
            s[i]=s[i][0].upper() + s[i][1:]
            if len(s[i]) <= 2:
                s[i]=s[i].lower()
        result = " ".join(s)
        return result
                 

        
        
        
        