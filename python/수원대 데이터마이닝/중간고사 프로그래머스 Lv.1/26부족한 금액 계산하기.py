def solution(price, money, count):
    answer=0
    for iter in range(1, count+1):
        answer+=price*iter
    if answer<money:
        return 0
    return answer-money