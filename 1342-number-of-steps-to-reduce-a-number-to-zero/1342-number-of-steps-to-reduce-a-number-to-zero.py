class Solution(object):
    def numberOfSteps(self, num):
        count=0 
        n=num
        while (n > 0):
            if n % 2==0:
                n=n/2
                count+=1
            else:
                n=n-1
                count+=1
        return count

        