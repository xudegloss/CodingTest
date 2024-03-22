def solution(n):
    result=0 # count
    count=0 # 500번 반복 시 1 되지 않는 경우, -1 반환
    
    if n==1:
        return 1
    
    while True:
        if n%2==0: # 짝수
            n=n//2
            result+=1
            if n==1:
                return result
        else: # 홀수
            n=n*3+1
            result+=1
            if n==1:
                return result
        count+=1
        
        if count==500:
            return -1