def stockSell(prices):
    return sum(prices[i] - prices[i-1] if prices[i] > prices[i-1] else 0 for i in range(1, len(prices)))


prices = [2,5,4,8,6,3,1,4,7]
answer = 13

print(stockSell(prices) == answer)