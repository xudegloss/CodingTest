def solution(n):
    answer = ''
    repeat=n//2
    if n%2==0:
        answer="수박"*repeat
    else:
        answer="수박"*repeat+"수"
    return answer

print(solution(3))