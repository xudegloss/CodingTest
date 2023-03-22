def solution(n):
    answer = 0
    _list=[]
    for num in str(n):
        _list.append(num)
    _list=sorted(_list)[::-1]
    answer="".join(_list)
    return int(answer)
    
print(solution(118372))