arr=[4,3,2,1]
arr.sort(reverse=True)
print(arr)

def solution(arr):
    if (len(arr)==1) or (len(arr)==0):
        return [-1]
    
    ## 여러 개인 경우 고려하기.
    ## 이 부분 틀림. 정렬하라는 조건이 없었기 때문이다.
    arr.sort(reverse=True)
    answer=[i for i in arr if i!=arr[-1]]
    return answer

def solution(arr):
    if (len(arr)==1) or (len(arr)==0):
        return [-1]
    
    ## 여러 개인 경우 고려하기.
    min_num=min(arr)
    answer=[i for i in arr if i!=min_num]
    return answer

print(solution([1,1,1,2,3,2,4,4,5,2]))