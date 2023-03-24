def solution(n):
    answer = 0
    x=1
    # if n<=0:
    #     return -1
    # else:
    while True:
        if x**2==n:
            answer=(x+1)**2
            break
        else:
            x+=1
            if x>n:
                return -1
    return answer

print(solution(121))