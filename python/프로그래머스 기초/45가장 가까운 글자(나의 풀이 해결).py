def solution(s):
    stack=[]
    answer = []

    for char in s:
        if char not in stack:
            stack.append(char)
            answer.append(-1)
        else:
            mid=0
            for s in stack[::-1]:
                if char!=s:
                    mid+=1
                else:
                    mid+=1
                    break
            stack.append(char)
            answer.append(mid)
    return answer

print(solution("banana"))
