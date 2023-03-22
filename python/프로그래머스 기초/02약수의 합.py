def solution(n):
    answer = 0
    for ii in range(1, n+1):
        if n%ii==0:
            answer+=ii
    return answer

print(solution(12))