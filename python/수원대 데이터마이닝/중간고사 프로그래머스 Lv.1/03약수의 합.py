# 12 : 1, 2, 3, 4, 6, 12 : 28
# 1. 약수를 구한다.
# 2. 모두 더하여 반환한다.

def solution(n):
    answer = 0
    for num in range(1, n+1):
        if n%num==0:
            answer+=num
    return answer

# 리스트 컴프리헨션 이용하기.

def solution(n):
    return sum([num for num in range(1, n+1) if n%num==0])