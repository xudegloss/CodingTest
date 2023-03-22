def solution(n):
    answer = []
    for idx in range(len(str(n))-1, -1, -1):
        print(idx)
        answer.append(int(str(n)[idx]))
    return answer

print(solution(12345))