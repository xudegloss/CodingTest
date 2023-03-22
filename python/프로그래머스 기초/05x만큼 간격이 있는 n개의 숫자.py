def solution(x, n):
    answer = []
    plus=0
    for iter in range(n):
        plus+=x
        answer.append(plus)
    return answer

print(solution(2, 5))