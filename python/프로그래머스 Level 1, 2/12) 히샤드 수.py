def solution(x):
    num = sum([int(str(x)[i]) for i in range(0, len(str(x)))])
    if x%num==0:
        return True
    return False