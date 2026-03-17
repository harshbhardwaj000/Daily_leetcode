class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        arr=list(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] in arr:
                arr.remove(ransomNote[i])
            else:
                return False
        return True
            
        
        