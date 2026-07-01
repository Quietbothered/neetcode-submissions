class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        suffix = [0]*len(prices)
        suffix[-1] = prices[-1]
        if len(prices) == 0 or len(prices)==1 :
            return 0
        else:
            for i in range(-1, -len(prices)-1,-1):
                suffix[i]= max(suffix[i+1],prices[i])
            for i in range(len(prices)):
                suffix[i]=max(0,suffix[i]-prices[i])
            return max(0,max(suffix[i] for i in range(len(suffix))))