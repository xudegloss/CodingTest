def solution(n):
    answer = []
    # 1. 10진법에서 뒤집은 3진법으로 변경하기.
    while n>2:
        answer.append(n%3)
        n=n//3
    answer.append(n)
    
    # 2. 뒤집힌 3진법에서 10진법으로 변경하기.
    result=0
    for idx in range(0, len(answer)):
        result+=(3**idx)*answer[len(answer)-1-idx]
    return result

print(solution(125))
