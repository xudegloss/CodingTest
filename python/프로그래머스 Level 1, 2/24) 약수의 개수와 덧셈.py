# 약수의 개수가 짝수인 경우, +
# 약수의 개수가 홀수인 경우, -

def solution(left, right):
    _list=[]
    for n in range(left, right+1):
        count=0
        for m in range(1, n+1):
            if n%m==0:
                count+=1
        _list.append(count)
    
    answer=0
    standard=[i for i in range(left, right+1)]
    
    for idx in range(len(_list)):
        if _list[idx]%2==0: # 짝수
            answer+=standard[idx]
        else:
            answer-=standard[idx]
    return answer