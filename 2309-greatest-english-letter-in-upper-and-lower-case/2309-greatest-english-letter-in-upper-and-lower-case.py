class Solution(object):
    def greatestLetter(self, s):
        upper = set()
        lower = set()
        for x in s:
            if x.isupper():
                upper.add(x)
            elif x.islower():
                lower.add(x)
        for x in upper.copy():
            if x.lower() not in lower:
                upper.remove(x)
        return max(upper) if upper else ""

        

        