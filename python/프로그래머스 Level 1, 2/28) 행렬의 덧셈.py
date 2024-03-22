def solution(arr1, arr2):
    result=[]
    for i, v in enumerate(arr1):
    # i는 행 인덱스 의미
    # j는 열 인덱스 의미
        answer=[]
        for j in range(len(v)):
            answer.append(v[j] + arr2[i][j])
        result.append(answer)
    return result