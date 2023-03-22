def solution(n):
    answer = 0
    for idx in range(len(str(n))):
        answer+=int(str(n)[idx])
    return answer

print(solution(123))