def maxProfit(prices):
    answer=0
    for idx in range(0, len(prices)-2):
        if prices[idx]<prices[idx+1]:
            answer+=(prices[idx+1]-prices[idx])
        else:
            continue
    return answer
    pass

# 아래는 수정하지 마시오.
prices01 = [7,1,5,3,6,4]
print(maxProfit(prices01))