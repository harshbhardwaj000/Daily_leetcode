class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        count = 0
        for i in range(len(cost)):
            if i%3 != 2:
                count+= cost[i]
        return count
        