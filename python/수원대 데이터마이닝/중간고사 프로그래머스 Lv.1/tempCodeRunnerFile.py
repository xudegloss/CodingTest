def solution(arr1, arr2):
    answer=[]
    for i in range(0, len(arr1)):
        mid_answer=[]
        for j in range(0, len(arr1)):
            mid_answer.append(arr1[i]+arr2[j])
        print(mid_answer)

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))