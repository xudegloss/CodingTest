def solution(a, b):
    ## a가 b보다 더 큰 경우
    if a>b:
        a,b=b,a
    answer=0
    for num in range(a, b+1):
        answer+=num
    return answer