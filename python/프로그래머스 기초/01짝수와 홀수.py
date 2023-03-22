def solution(num):
    answer = ''
    if num%2==0:
        answer="Even"
    else: # else 안 적어주면 if문 성립해도 다시 그 명령문을 수행한다.
        answer="Odd"
    return answer

print(solution(3))