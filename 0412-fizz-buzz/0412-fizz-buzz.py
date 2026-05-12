class Solution(object):
    def fizzBuzz(self, n):
        arr=[]
        for i in range(1,n+1):
            if i % 3==0 and i % 5 ==0:
                arr.append(str("FizzBuzz"))
            elif i % 3==0:
                arr.append(str("Fizz"))
            elif i % 5==0:
                arr.append(str("Buzz"))
            else:
                arr.append(str(i))
        return arr
