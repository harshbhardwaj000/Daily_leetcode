class Solution(object):
    def bitwiseComplement(self, n):
        m=bin(n)[2:]
        v=[]
        for i in m:
            if i == '0':
                v.append("1")
            else:
                v.append("0")
        return int("".join(v), 2)
        
        