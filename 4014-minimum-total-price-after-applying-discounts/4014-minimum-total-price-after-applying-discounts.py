class Solution(object):
    def minPrice(self, prices, discounts):
        # final_sum = 0
        n = len(prices)
        m = len(discounts)
        k= n-m
        prices.sort(reverse=True)
        if k > 0:
            dis = sorted(discounts,reverse=True) + [0]*k
        else:
            dis = sorted(discounts,reverse=True)
        
        # for i in range(len(prices)):
        #     avg = (prices[i]*(100-dis[i])) / 100.0
        #     final_sum += avg
        # return final_sum
        return sum([p * (100 - d) / 100.0 for p, d in zip(prices, dis)])


        