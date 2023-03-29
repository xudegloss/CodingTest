# # 지도 그리기.
# arr1=[46, 33, 33 ,22, 31, 50]
# arr1_answer=[]

# for iter in range(0, len(arr1)):
#     arr1_result=[]
#     for mw in range(len(arr1)-1, -1, -1): # 역순으로
#         if arr1[iter]<2**mw:
#             arr1_result.append(0)
#         else:
#             arr1_result.append(1)
#             arr1[iter]=arr1[iter]%(2**mw)

#     arr1_answer.append(arr1_result)

# arr2=[27 ,56, 19, 14, 14, 10]
# arr2_answer=[]

# for iter in range(0, len(arr2)):
#     arr2_result=[]
#     for mw in range(len(arr2)-1, -1, -1):
#         if arr2[iter]<2**mw:
#             arr2_result.append(0)
#         else:
#             arr2_result.append(1)
#             arr2[iter]=arr2[iter]%(2**mw)
    
#     arr2_answer.append(arr2_result)

# answer=[]
# # string 부분 주의하기.
# string=str("".join([str(i) for i in range(0, len(arr1_answer))]))

# for idx, arr1, arr2 in zip(string, arr1_answer, arr2_answer):
#     mid_answer=[]
#     for i in range(0, len(arr1_answer)):
#         if (arr1[i]==0) and (arr2[i]==0):
#             mid_answer.append(" ")
#         else:
#             mid_answer.append("#")
#     answer.append("".join(mid_answer))

# print(answer)

def solution(n, arr1, arr2):
    arr1_answer=[]
    arr2_answer=[]
    answer=[]

    for iter in range(0, len(arr1)):
        arr1_result=[]
        for mw in range(len(arr1)-1, -1, -1): # 역순으로
            if arr1[iter]<2**mw:
                arr1_result.append(0)
            else:
                arr1_result.append(1)
                arr1[iter]=arr1[iter]%(2**mw)

        arr1_answer.append(arr1_result)


    for iter in range(0, len(arr2)):
        arr2_result=[]
        for mw in range(len(arr2)-1, -1, -1):
            if arr2[iter]<2**mw:
                arr2_result.append(0)
            else:
                arr2_result.append(1)
                arr2[iter]=arr2[iter]%(2**mw)
    
        arr2_answer.append(arr2_result)
        
    string="".join([str(i) for i in range(0, len(arr1_answer))])
    for idx, arr1, arr2 in zip(string, arr1_answer, arr2_answer):
        mid_answer=[]
        for i in range(0, len(arr1)):
            if (arr1[i]==0) and (arr2[i]==0):
                mid_answer.append(" ")
            else:
                mid_answer.append("#")
        answer.append("".join(mid_answer))

    return answer