def solution(s):
    if len(s) >= 1:
        return "".join(sorted(s, reverse=True))