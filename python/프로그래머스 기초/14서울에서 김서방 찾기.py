def solution(seoul):
    answer = ''
    # 반복문 대신 .index("Kim") 사용 가능하다.
    for idx in range(len(seoul)):
        if seoul[idx]=="Kim":
            answer=f'김서방은 {idx}에 있다'
    return answer

print(solution(["Jane", "Kim"]))