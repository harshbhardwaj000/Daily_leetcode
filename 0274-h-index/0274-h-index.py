class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        citations.sort()

        for i in range(n):
            h = n - i
            if citations[i] >= h:
                return h
        return 0
      