class Solution(object):
    def processStr(self, s):
        result=[]
        
        for ch in s:
            if ch not in "*#%":
                result.append(ch)
            elif ch == "*":
                if result:
                    result.pop()
            elif ch == "#":
                result = result + result
            elif ch == "%":
                result= result[::-1]
        # if not result:
        #         return s
        return "".join(result)
        