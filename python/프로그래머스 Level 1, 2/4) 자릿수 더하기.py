def solution(N):
    answer=0
    for idx in range(len(str(N))):
        answer+=int(str(N)[idx])
    return answer