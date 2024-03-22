def solution(a, b):
    answer=0
    for idx in range(len(a)):
        sub_ans=a[idx]*b[idx]
        answer+=sub_ans
    return answer