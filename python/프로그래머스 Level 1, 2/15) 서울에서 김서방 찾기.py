# f-string (format)

def solution(seoul):
    for idx in range(0, len(seoul)):
        if seoul[idx]=="Kim":
            return "김서방은 {}에 있다".format(idx)