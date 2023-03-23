def solution(absolutes, signs):
    answer=0
    for idx in range(len(signs)):
        if signs[idx]: # true
            answer+=absolutes[idx]
        else: # false
            answer-=absolutes[idx]
    return answer

