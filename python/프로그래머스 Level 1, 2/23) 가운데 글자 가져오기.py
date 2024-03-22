def solution(s):
    if len(s)%2==1: # 홀수
        return s[int(len(s))//2]
    else: # 짝수
        return s[int(len(s))//2-1:int(len(s))//2+1]