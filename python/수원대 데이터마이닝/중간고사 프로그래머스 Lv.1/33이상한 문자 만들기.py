def solution(s):
    s=s.split(" ")  
    answer=[]

    for words in s:
        for idx in range(0, len(words)):
            if idx%2==0:
                answer.append(words[idx].upper())
            else:
                answer.append(words[idx].lower())
        answer.append(" ")
    return "".join(answer[:-1])

## 왜 rstrip은 안될까? 질문 올려놨음.