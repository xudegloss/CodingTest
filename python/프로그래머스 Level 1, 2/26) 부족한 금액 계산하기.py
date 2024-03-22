# 금액 부족하지 않으면 0 출력
# 필요한 금액 만큼 출력

# price : 이용료
# money : 가지고 있는 예산
# count : 놀이기구 이용 횟수

def solution(price, money, count):
    answer = 0 # 총 이용 금액
    
    for n in range(1, count+1):
        answer+=price*n
    
    if answer > money:
        return answer-money
    return 0