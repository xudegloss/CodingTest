def solution(s):
    stack=[]
    answer = []

    for char in s:
        if char not in stack:
            stack.append(char)
            answer.append(-1)
        else:
            stack.append(char)
            answer.append(char)
    return answer

print(solution("banana"))