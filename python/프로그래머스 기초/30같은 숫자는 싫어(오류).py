def solution(arr):
    answer=[]
    for idx in range(0, len(arr)-1):
        # print(arr[idx], arr[idx+1])
        if (arr[idx]==arr[idx+1]) and (((arr[idx] not in answer) or (answer[-1]!=arr[idx]))):
            answer.append(arr[idx])
        else:
            if arr[idx] not in answer:
                answer.append(arr[idx])
            elif arr[idx+1] not in answer:
                answer.append(arr[idx+1])
    return answer

print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))

# 중복 제거하는 방법
# def solution(arr):
#     my_arr=[]
#     for val in arr:
#         if val not in my_arr:
#             my_arr.append(val)
#     return my_arr

# print(solution([1, 1, 3, 3, 0, 1, 1]))
# print(solution([4, 4, 4, 3, 3]))