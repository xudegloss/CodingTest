# 1. i번째 ~ j번째 배열 가져오기.
# 2. 새로운 배열 정렬하기.
# 3. k번째 요소 찾아서 리스트에 넣어주기.

# arr=[1, 5, 2, 6, 3, 7, 4]
# commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# answer=[]

# for iter in range(0, len(commands)):
#     i,j,k=commands[iter][0], commands[iter][1], commands[iter][2]
#     sorted_commands=sorted(arr[i-1:j])
#     if len(sorted_commands)==1:
#         answer.append(sorted_commands[0])
#     else:
#         answer.append(sorted_commands[k-1])

# print(answer)

# def solution(array, commands):
#     answer = []
#     for iter in range(0, len(commands)):
#         # 구조 분해 할당
#         i,j,k=commands[iter][0], commands[iter][1], commands[iter][2]
#         sorted_commands=sorted(array[i-1:j])
#         if len(sorted_commands)==1:
#             answer.append(sorted_commands[0])
#         else:
#             answer.append(sorted_commands[k-1])
#     return answer

def solution(array, commands):
    answer = []
    for iter in range(0, len(commands)):
        # 구조 분해 할당
        i,j,k=commands[iter][0], commands[iter][1], commands[iter][2]
        sorted_commands=sorted(array[i-1:j])
        answer.append(sorted_commands[k-1])
    return answer