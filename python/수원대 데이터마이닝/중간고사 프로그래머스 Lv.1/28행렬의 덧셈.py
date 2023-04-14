def solution(arr1, arr2):
    answer=[]
    for i in range(0, len(arr1)):
        mid_answer=[]
        ## arr1 대신 arr1[i] 넣어주기!
        for j in range(0, len(arr1[i])):
            mid_answer.append(arr1[i][j]+arr2[i][j])
        answer.append(mid_answer)
    return answer

print(solution([[1],[2]], [[3],[4]]))