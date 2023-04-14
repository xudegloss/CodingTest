def solution(n):
    answer = 0
    n=str(n)
    for idx in range(0, len(n)):
        answer+=int(n[idx])
    return answer

# 리스트 컴프리헨션 이용하기.

def solution(n):
    n=str(n)
    return sum([int(n[idx]) for idx in range(0, len(n))])