# 무한 반복문 대신에 range(1, 500) 이용하는 방법 이용하기.
def solution(num):
    if num==1:
        return 0
    
    for iter in range(1, 500):
        if num%2==0:
            num=num//2
            if num==1:
                return iter
        else:
            num=num*3+1
            if num==1:
                return iter
    return -1

print(solution(6))

        