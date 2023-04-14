def solution(n):
    if n==1:
        return "수"
    
    if n%2==0:
        return "수박"*(n//2)
    else:
        return "수"+"박수"*(n//2)
    
print(solution(3))
print(solution(4))
