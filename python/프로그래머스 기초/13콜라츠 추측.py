def solution(num):
    answer = 0
    iter=0
    while True:
        if num==1:
            return 0
        
        if num%2==0: # even
            num=num//2
            iter+=1
        else:
            num=num*3+1
            iter+=1

        if num==1:
            answer=iter
            break
        if iter==500:
            return -1
        
    return answer