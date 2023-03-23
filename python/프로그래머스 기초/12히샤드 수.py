def solution(x):
    answer = True
    divide=0
    for idx in range(len(str(x))):
        divide+=int(str(x)[idx])
    if x%divide==0:
        answer=True
    else:
        answer=False
    return answer

print(solution(10))
