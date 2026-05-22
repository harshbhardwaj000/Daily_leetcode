class Solution(object):
    def myAtoi(self, s):
        i,n=0,len(s)
        max_len= 2**31-1
        min_len= -2**31

        while i < n and s[i] ==" ":###to aboid blank space
            i +=1

        sign = 1 
        if i < n and (s[i] =="+" or s[i] =="-"):# to handle "+" & "-"
            sign = -1 if s[i] =="-" else 1
            i +=1

        if i >= n or not s[i].isdigit():
            return 0

        num = 0
        while i < n and s[i].isdigit():#read digit
            digit = ord(s[i]) - ord("0") 

            if num > (max_len - digit) // 10:
                return max_len if sign == 1 else min_len
            
            num = num * 10 + digit
            i += 1
        
        return sign*num


        