def solution(n):
    n=str(n)
    n=list(n)
    n.sort(reverse=True)
    return int("".join(n))