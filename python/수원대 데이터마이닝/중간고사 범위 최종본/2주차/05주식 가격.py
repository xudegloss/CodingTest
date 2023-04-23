def maxProfit(prices):
    result=0
    for idx in range(0, len(prices)-1):
        if prices[idx]<prices[idx+1]:
            result+=(prices[idx+1] - prices[idx])
        else:
            continue
    return result
    pass

# 아래는 수정하지 마시오.
prices01 = [7,1,5,3,6,4]
print(maxProfit(prices01))