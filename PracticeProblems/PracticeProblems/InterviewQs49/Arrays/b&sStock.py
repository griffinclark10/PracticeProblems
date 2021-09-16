#given an array of prices for the ith day, tell me when I should buy and sell stocks to make the biggest profit

#O(n^2):
def maxProfit1(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        profit = 0
        for i in range(len(prices)-1):
            for j in range(len(prices)-1, i, -1):
                #print(i, j)
                a = prices[j] - prices[i]
                if a > profit:
                    profit = a
        return profit


#realizing that this is not actually the correct answer, I was supposed to find the solution that allows for the max profit
#a better solution that I found in the discussion:

def maxProfit(prices) -> int:
        if len(prices) == 1: # edge case
            return 0
        
        # take down positive daily return only
        profit = [] 
        for i in range(1, len(prices)):
            profit.append(max(0, prices[i] - prices[i-1])) #append either 0 or p[i] - p[i-1] depending on which is max
        return sum(profit) #sum the array

#testing:
test = [7,1,5,3,6,4]
print(maxProfit(test))