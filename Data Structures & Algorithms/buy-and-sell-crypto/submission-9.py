class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # res = 0 

        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i+1,len(prices)):
        #         sell = prices[j]
        #                1 - 7 = -6
        #         res = max(res, sell - buy)

        # return res

        # two pointers
        l = 0
        r = 1
        Mprofit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                buy = prices[l]
                sell = prices[r]
                profit = sell - buy

                Mprofit = max(Mprofit, profit)

               
            else:
                l = r

            r +=1

        return Mprofit
            
         

        # 7 1 5 3 6 4
          # l 
               # r
        # [2,1,2,1,0,1,2]
        #          l   r
        # l = 0 
        # r = 1
        # res = 0 
        # while r < len(prices):
        #     if prices[l] > prices[r]:
        #         l = r
        #     else:
        #         res = max(res, prices[r] - prices[l])
        #     r += 1
        # return res


#Keep track of the cheapest price seen so far, and at each day check how much profit you’d make by selling that day.

# l = best/cheapest day to buy so far
# r = current day you’re considering selling
# If prices[r] < prices[l] → found a cheaper buy, so l = r
# Otherwise → calculate prices[r] - prices[l] and update max profit

# Easy memory trick:

# Buy as low as possible, then test every future sell price.

# Time: O(n), Space: O(1).
