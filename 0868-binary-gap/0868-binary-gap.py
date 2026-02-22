class Solution(object):
    def binaryGap(self, n):
        max_dis = 0
        binary=bin(n)[2:]
        last = -1
        for i in range(len(binary)):
            if binary[i] == '1':
                if last != -1:
                    max_dis=max(max_dis,i-last)
                last = i
        return max_dis
               
                





        