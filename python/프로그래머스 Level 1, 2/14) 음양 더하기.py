def solution(absolutes, signs):
    answer=0
    for idx in range(0, len(signs)):
        if signs[idx]==True:
            answer+=absolutes[idx]
        else:
            answer-=absolutes[idx]
    return answer