def solution(s):
    if len(s)>=1 and len(s)<=5:
        if s in "-":
            return "-"+int(s[1:])
        return int(s)