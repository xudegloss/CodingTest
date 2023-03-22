def solution(s):
    answer = True
    p_count=0
    y_count=0
    for num in s:
        if num=="p" or num=="P":
            p_count+=1
        if num=="y" or num=="Y":
            y_count+=1
    if p_count==y_count:
        answer=True
    else:
        answer=False
    return answer

print(solution("Pyy"))