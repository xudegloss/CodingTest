def solution(n):
    _list=[]
    for i in range(1, n+1):
        if n%i==0:
            _list.append(i)
        else:
            continue
    return sum(_list)