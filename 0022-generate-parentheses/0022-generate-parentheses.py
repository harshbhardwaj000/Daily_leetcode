class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        arr = []

        def backprop(openn,closen):
            if openn == closen == n:
                arr.append("".join(stack))
                return
            
            if openn < n:
                stack.append("(")
                backprop(openn +1,closen)
                stack.pop()

            if closen < openn:
                stack.append(")")
                backprop(openn, closen +1)
                stack.pop()

        backprop(0,0)
        return arr