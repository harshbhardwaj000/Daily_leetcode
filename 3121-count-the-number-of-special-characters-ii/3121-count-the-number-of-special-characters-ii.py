class Solution(object):
    def numberOfSpecialChars(self, word):
        # hashtable = {}
        # count=0
        # for index, ch in enumerate(word):
        #     hashtable[ch] = index        ###{'h':0,'e':1}
        # for key in hashtable:
        #     low_key = key.lower()
        #     if key.isupper() and low_key in hashtable:
        #         if hashtable[low_key] < hashtable[key]:
        #             count+=1 
        # return count
        low={}
        up={}
        for i,ch in enumerate(word):
            if ch.islower():
                low[ch] =i
            else:
                if ch not in up:
                    up[ch] = i
        count = 0
        for ch in low:
            upp = ch.upper()
            if upp in up and low[ch] < up[upp]:
                count +=1
        return count
                    

        
        