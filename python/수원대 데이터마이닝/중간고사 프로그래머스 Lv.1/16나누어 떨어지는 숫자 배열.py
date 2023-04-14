def solution(arr, divisor):
    answer=[arr[idx] for idx in range(0, len(arr)) if arr[idx]%divisor==0]
    answer.sort()
    if answer==[]:
        return [-1]
    return answer

print(solution([3,2,6], 10))