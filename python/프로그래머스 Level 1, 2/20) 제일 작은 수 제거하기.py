## 1 ##
# test case 1개가 "시간 초과"

def solution(arr):
    answer=[]
    if len(arr)==1:
        return [-1]
    for n in arr:
        if n != min(arr):
            answer.append(n)
    return answer


## 2 ##
# remove 함수 이용하기.

def solution(arr):
    if len(arr)<=1:
        return [-1]
    arr.remove(min(arr))
    return arr