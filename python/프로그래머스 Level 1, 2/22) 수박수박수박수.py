# "".join(리스트 → 문자열로 만들기 위함)

def solution(n):
    answer=[]
    for idx in range(n):
        if idx%2==0: # idx 짝수
            answer.append("수")
        else: # idx 홀수
            answer.append("박")
    return "".join(answer)