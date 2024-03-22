## 풀이 과정 확인 → 틀렸다고 나옴 ##

def solution(s):
    answer = []
    s = s.split(" ") # s → list
    for word in s:
        if word: # 문자인 경우
            answer.append(word[0].upper() + word[1:].lower())
        else: # 숫자가 섞인 경우
            answer.append(word.lower())
    return " ".join(answer)


def answer_solution(s):
    answer =[]
    for i in range(len(s.split())):
        answer.append(s.split()[i][0].upper() + s.split()[i].lower()[1:]) 
    return " ".join(answer)


def solution(s):
    answer=[]
    for i in range(len(s.split())):
        answer.append(s.split()[i][0].upper() + s.split()[i].lower()[1:])
    return " ".join(answer)


"""
    ## 이게 왜 안 되는지 모르겠음 ##
    
    def solution(s):
        s=s.split()
        answer=[]
        for idx in range(len(s)):
            answer.append(s[idx][0].upper()+s[idx][1:].lower())
        return " ".join(answer)
    
"""