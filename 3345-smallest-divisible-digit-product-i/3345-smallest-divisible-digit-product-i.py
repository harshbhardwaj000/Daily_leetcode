class Solution(object):
    def smallestNumber(self, n, t):
        # for i in range(10):
        #     for j in range(10):
        #         if i >= n and i % t ==0:
        #             return i
        #         result="".join([str(i),str(j)])
        #         if int(result) >= n:
        #             if (i*j) % t == 0:
        #                 return int(result)
        # return None
        while True:
            product = 1
            x = n
            while x > 0:
                product *= x%10
                x//=10
            if product % t == 0:
                return n
            n+=1



        