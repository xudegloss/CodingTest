# import math
# print(math.sqrt(121)==int(math.sqrt(121)))
# print(math.sqrt(3)==int(math.sqrt(3)))

def solution(n):
    ## 0보다 작은 수가 들어오는 경우에도 -1 반환해야 한다.
    if n<=0:
        return -1
    
    sqrt=n**(1/2)
    if sqrt==int(sqrt):
        return (sqrt+1)**2
    return -1
