def solution(s):
    if len(s)%2==0: # even
        idx=len(s)//2
        return s[idx-1: idx+1]
    else:
        idx=len(s)//2
        return s[idx]