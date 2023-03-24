def solution(price, money, count):
    price_sum=0
    for iter in range(1, count+1):
        price_sum+=price*iter
    result= price_sum-money
    # 금액이 부족하지 않으면 0을 반환한다.
    if(result<0): 
        return 0
    return result

print(solution(30, 20, 4))