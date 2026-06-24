class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}

        for ch in s:
            # if opening bracket -> push to stack
            if ch in "({[":
                stack.append(ch)
            else:
                # if closing bracket but stack empty -> invalid
                if not stack:
                    return False
                # check top of stack
                if stack[-1] == mapping[ch]:
                    stack.pop()
                else:
                    return False
        
        # valid only if stack empty at end
        return len(stack) == 0