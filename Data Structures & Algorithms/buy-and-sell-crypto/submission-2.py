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
         

        # 7 1 5 3 6 4
        # l r
             
        l = 0 
        r = 1
        res = 0 
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
            r += 1
        return res
