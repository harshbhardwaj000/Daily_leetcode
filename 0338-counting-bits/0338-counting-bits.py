class Solution(object):
    def countBits(self, n):
        arr = []
        for i in range(n+1):
            binary=bin(i).count('1')
            arr.append(binary)
        return arr


        