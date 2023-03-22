def solution(n):
    answer = 0
    for div in range(1, n):
        if n%div==1:
            answer=div
            break
    return answer

print(solution(12))