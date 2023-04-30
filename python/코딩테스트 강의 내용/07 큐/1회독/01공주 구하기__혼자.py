def solution(n, k):
    answer_list=[num for num in range(1, n+1)]
    
    while len(answer_list)>k-1:
        answer_list=answer_list[k:]+answer_list[:k-1]
    return answer_list
    # 생각한 대로 코드를 짜봤는데, 그 뒤로 어떻게 해야할지 모르겠다.

print(solution(8, 3))