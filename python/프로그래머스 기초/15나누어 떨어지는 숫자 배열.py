# sort 함수 이용하기.
def solution(arr, divisor):
    answer = []
    arr.sort()
    for num in arr:
        if num%divisor==0:
            answer.append(num)
    if answer==[]:
        return [-1]
    return answer

print(solution([3,2,6], 10))
