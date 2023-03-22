def solution(arr):
    answer = 0
    _sum=0
    for num in arr:
        _sum+=num
    answer=_sum/len(arr)
    return answer

print(solution([1,2,3,4]))