# mat=[[1,2], [3,4]]
# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#         print(mat[i][j])

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        row=[]
        for j in range(len(arr1[i])):
            row.append(arr1[i][j]+arr2[i][j])
        answer.append(row)
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
