class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        if len(arr1) > len(arr2):
            arr1,arr2 = arr2,arr1
        
        pre_set = set()
        for n in arr1:
            while n and n not in pre_set:
                pre_set.add(n)
                n = n//10
        count = 0
        for n in arr2:
            while n and n not in pre_set:
                n = n//10
        
            if n:
                count =  max(count,len(str(n)))
        return count




        