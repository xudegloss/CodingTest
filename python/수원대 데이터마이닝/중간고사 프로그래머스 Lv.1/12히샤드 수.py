def solution(x):
    x=str(x)
    divide=sum([int(x[idx]) for idx in range(0, len(x))])
    if int(x)%divide==0:
        return True
    return False