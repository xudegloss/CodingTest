def solution(arr):
    # 1. 일단 stack에 넣기.
    # 2. stack 안에 동일한 숫자 있으면 제거하기.
    answer=[arr[0]]
    for idx in range(1, len(arr)):
        answer.append(arr[idx])
        if arr[idx-1]==answer[-1]:
            answer.pop()
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))
